from fastapi import APIRouter

router = APIRouter(prefix="/expense", tags=["Expenses"])

# Creating an expense
@router.post("/")
def createExpense():
    return {
        "message":"Expense Created Successfully"
    }

# retrive expenses
@router.get("/{id}")
def getExpense():
    return {
        "message" : "Expense Retrived"
    }

#update expense
@router.put("/{id}")
def updateExpense():
    return {
        "message" : "Expense Updated"
    }

#delete expense
@router.delete("/{id}")
def deleteExpense():
    return {
        "message" : "Expense Deleted"
    }