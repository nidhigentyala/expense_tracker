from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    id : int
    title: str
    amount: int
    category: str 
    date: str 
    user_id: int
    user_name: str


class UpdateExpense(ExpenseCreate):
    id : int
    title: str
    amount: int
    category: str
    date: str 
    user_id: int
    user_name: str

class BudgetCreate(BaseModel):
    budget_id : int
    budget_amount : int
    total_spent : int
    remaining_amt : int
    month : str
    user_id: int
    user_name: str

class ExpenseCreateError(BaseModel):
    message: str
    status_code: int