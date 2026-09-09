from pydantic import BaseModel, Field
from typing import Optional
import datetime

class AddExpense(BaseModel):
    expense_id: int = Field(..., description="Unique identifier for the expense")
    expense_title: str = Field(..., min_length=3, max_length=100,description="Type of expense")
    amount: float = Field(..., gt=0, description="Amount paid")
    category: str = Field(..., min_length=3, max_length=100,description="category of expense")
    paid_by: str = Field(..., min_length=3, max_length=100,description="Who paid")
    sharing: list[str] = Field(..., min_length=1, description="People sharing the expense")
    date: datetime.datetime = Field(..., description="Date of payment ")
    description: Optional[str] = Field(default=None, min_length=3, max_length=100, description="description for the expense")

class CreateExpense(AddExpense):
    pass

class UpdateExpense(BaseModel):
    expense_title: Optional[str] = Field(default=None, min_length=3, max_length=100,description="Type of expense")
    amount: Optional[float] = Field(default=None, gt=0, description="Amount paid")
    category: Optional[str] = Field(default=None, min_length=3, max_length=100,description="category of expense")
    paid_by: Optional[str] = Field(default=None, min_length=3, max_length=100,description="Who paid")
    sharing: Optional[list[str]] = Field(default=None, min_length=1, description="People sharing the expense")
    date: Optional[datetime.datetime] = Field(default=None, description="Date of payment ")
    description: Optional[str] = Field(default=None, min_length=3, max_length=100,description="description for the expense")

class MessageResponse(BaseModel):
    message: str

class ExpenseResponse(AddExpense):
    id:str = Field(..., description="The ID of the Expense")
    model_config = {
        "json_schema_extra": {
            "example":{
                "id": "123",
                "expense_title": "Lunch",
                "amount": 20.5,
                "category": "Food",
                "paid_by": "John",
                "sharing": ["John", "Doe"],
                "date": "2024-06-01T12:00:00Z",
                "description": "Lunch at the cafe"
            }
        }
    }