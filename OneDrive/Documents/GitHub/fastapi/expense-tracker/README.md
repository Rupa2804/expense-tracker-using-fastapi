# Expense Tracker API

This beginner-friendly FastAPI project stores trips and their expenses in MongoDB.

## Run

1. Start MongoDB.
2. Set the values in `.env`.
3. Run `uv run uvicorn main:app --reload`.
4. Open `http://127.0.0.1:8000/docs`.

## Endpoint report

| Method | Endpoint | Purpose | Success |
| --- | --- | --- | --- |
| GET | `/health` | Check that the API is running | 200 |
| POST | `/trip/` | Create a trip | 201 |
| GET | `/trip/{id}` | Get one trip by `trip_id` | 200 |
| PUT | `/trip/{id}` | Update one or more trip fields | 200 |
| DELETE | `/trip/{id}` | Delete a trip | 200 |
| POST | `/expense/` | Create an expense | 201 |
| GET | `/expense/{id}` | Get one expense by `expense_id` | 200 |
| PUT | `/expense/{id}` | Update one or more expense fields | 200 |
| DELETE | `/expense/{id}` | Delete an expense | 200 |

Missing records return `404`, duplicate IDs return `409`, empty updates return `400`,
and invalid request data returns `422`.

## Tests

Run all endpoint tests with:

```text
uv run pytest
```

The tests use an in-memory fake collection, so MongoDB is not needed for testing.