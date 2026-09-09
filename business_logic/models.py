from pydantic import BaseModel

from dataacces.models import Expense,Budget


class ExpenseCreate(BaseModel):
    title: str
    amount: int
    category: str
    date: str

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date
        )

class UpdateExpense(ExpenseCreate):
    title: str
    amount: int
    category: str 
    date: str 

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date
        )
    

class BudgetCreate(BaseModel):
    budget_amount : int
    total_spent : int
    remaining_amt : int
    month : str

    @classmethod
    def from_db(cls, db_model: Budget):
        return cls (
            budget_amount = db_model.budget_amount,
            total_spent = db_model.total_spent, 
            remaining_amt = db_model.remaining_amt,
            month = db_model.month
        )
    
###### Business Logic Model (Pydantic)