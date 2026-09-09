from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient

from main import app
from services import expenseService, tripService
from utils import database


class Result:
    def __init__(self, matched_count=0, deleted_count=0):
        self.matched_count = matched_count
        self.deleted_count = deleted_count


class FakeCollection:
    def __init__(self):
        self.documents = {}

    def insert_one(self, document):
        key_name = "trip_id" if "trip_id" in document else "expense_id"
        key = document[key_name]
        if key in self.documents:
            from pymongo.errors import DuplicateKeyError

            raise DuplicateKeyError("duplicate")
        stored = dict(document)
        stored["_id"] = f"{key_name}-{key}"
        self.documents[key] = stored

    def find_one(self, query):
        key = next(iter(query.values()))
        document = self.documents.get(key)
        return dict(document) if document else None

    def update_one(self, query, update):
        key = next(iter(query.values()))
        if key not in self.documents:
            return Result()
        self.documents[key].update(update["$set"])
        return Result(matched_count=1)

    def delete_one(self, query):
        key = next(iter(query.values()))
        if key not in self.documents:
            return Result()
        del self.documents[key]
        return Result(deleted_count=1)


@pytest.fixture
def client(monkeypatch):
    trips = FakeCollection()
    expenses = FakeCollection()
    monkeypatch.setattr(database, "connect", lambda: None)
    monkeypatch.setattr(database, "disconnect", lambda: None)
    monkeypatch.setattr(tripService, "tripsCol", trips)
    monkeypatch.setattr(expenseService, "expensesCol", expenses)
    with TestClient(app) as test_client:
        yield test_client


def trip_payload(trip_id=1):
    return {
        "trip_id": trip_id,
        "trip_name": "Beach Trip",
        "destination": "Goa",
        "start_date": "2026-01-01T10:00:00Z",
        "end_date": "2026-01-05T10:00:00Z",
        "members": ["Rupa", "Sam"],
    }


def expense_payload(expense_id=1):
    return {
        "expense_id": expense_id,
        "expense_title": "Lunch",
        "amount": 20.5,
        "category": "Food",
        "paid_by": "Rupa",
        "sharing": ["Rupa", "Sam"],
        "date": datetime.now(timezone.utc).isoformat(),
        "description": "Lunch at the cafe",
    }


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Application Running"}


def test_trip_create_get_update_delete_endpoints(client):
    created = client.post("/trip/", json=trip_payload())
    assert created.status_code == 201
    assert created.json()["trip_id"] == 1

    fetched = client.get("/trip/1")
    assert fetched.status_code == 200
    assert fetched.json()["trip_name"] == "Beach Trip"

    updated = client.put("/trip/1", json={"destination": "Pune"})
    assert updated.status_code == 200
    assert updated.json()["trip_id"] == 1
    assert client.get("/trip/1").json()["destination"] == "Pune"

    deleted = client.delete("/trip/1")
    assert deleted.status_code == 200
    assert client.get("/trip/1").status_code == 404


def test_expense_create_get_update_delete_endpoints(client):
    created = client.post("/expense/", json=expense_payload())
    assert created.status_code == 201
    assert created.json()["expense_id"] == 1

    fetched = client.get("/expense/1")
    assert fetched.status_code == 200
    assert fetched.json()["expense_title"] == "Lunch"

    updated = client.put("/expense/1", json={"amount": 25})
    assert updated.status_code == 200
    assert updated.json()["expense_id"] == 1
    assert client.get("/expense/1").json()["amount"] == 25

    deleted = client.delete("/expense/1")
    assert deleted.status_code == 200
    assert client.get("/expense/1").status_code == 404


@pytest.mark.parametrize(
    "path,payload",
    [
        ("/trip/", {"trip_id": 1}),
        ("/expense/", {"expense_id": 1}),
    ],
)
def test_create_validation_errors(client, path, payload):
    response = client.post(path, json=payload)
    assert response.status_code == 422


@pytest.mark.parametrize("path", ["/trip/999", "/expense/999"])
def test_missing_records_return_not_found(client, path):
    assert client.get(path).status_code == 404
    assert client.put(path, json={}).status_code == 400
    assert client.delete(path).status_code == 404
