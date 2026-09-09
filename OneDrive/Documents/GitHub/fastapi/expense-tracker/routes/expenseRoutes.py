from fastapi import APIRouter, status
from schemas.expenseSchemas import CreateExpense, ExpenseResponse, UpdateExpense

from services.expenseService import create_Expense, delete_Expense, get_Expense, update_Expense

router = APIRouter(prefix="/expense", tags=["Expenses"])

# Creating an expense
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Expense_record(expense: CreateExpense):
    return create_Expense(expense)

# retrive expenses
@router.get("/{id}", response_model=ExpenseResponse)
def get_Expense_record(id: int):
    return get_Expense(id)

#update expense
@router.put("/{id}", status_code=200)
def update_Expense_record(id: int, expense: UpdateExpense):
    return update_Expense(id, expense)

#delete expense
@router.delete("/{id}", status_code=200)
def delete_Expense_record(id: int):
    return delete_Expense(id)