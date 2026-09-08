from pydantic import BaseModel, Field
from typing import Optional
import datetime

class AddExpense(BaseModel):
    expense_title: str = Field(..., min_length=3, max_length=100,description="Type of expense")
    amount: float = Field(...,description="Amount paid")
    category: str = Field(..., min_length=3, max_length=100,description="category of expense")
    paid_by: str = Field(..., min_length=3, max_length=100,description="Who paid")
    sharing: list = Field(..., description=" People sharing the expense")
    date: datetime.datetime = Field(..., description="Date of payment ")
    description: Optional[str] = Field(default=None, min_length=3, max_length=100,description="description for the expense") 