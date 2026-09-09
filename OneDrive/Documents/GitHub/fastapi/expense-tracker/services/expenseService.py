from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

from schemas.expenseSchemas import CreateExpense, UpdateExpense
from utils.database import get_collection


expensesCol = None


def _expenses_collection():
    return expensesCol if expensesCol is not None else get_collection("expenses")

def create_Expense(expense: CreateExpense):
    try:
        _expenses_collection().insert_one(expense.model_dump())
    except DuplicateKeyError as exc:
        raise HTTPException(status_code=409, detail="An expense with this expense_id already exists") from exc
    return {"message": "Expense Created Successfully", "expense_id": expense.expense_id}

def get_Expense(id: int):
    expense = _expenses_collection().find_one({"expense_id": id})
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense["id"] = str(expense["_id"])
    del expense["_id"]
    return expense

def update_Expense(id: int, expense: UpdateExpense):
    changes = expense.model_dump(exclude_unset=True)
    if not changes:
        raise HTTPException(status_code=400, detail="At least one field is required")
    result = _expenses_collection().update_one({"expense_id": id}, {"$set": changes})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense Updated", "expense_id": id}

def delete_Expense(id: int):
    result = _expenses_collection().delete_one({"expense_id": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense Deleted", "expense_id": id}