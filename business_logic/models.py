from pydantic import BaseModel

from dataacces.models import Expense,Budget


class ExpenseCreate(BaseModel):
    id : int
    title: str
    amount: int
    category: str
    date: str

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            id = db_model.id,
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date
        )

class UpdateExpense(ExpenseCreate):
    id : int
    title: str
    amount: int
    category: str 
    date: str 

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            id = db_model.id,
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date
        )
    

class BudgetCreate(BaseModel):
    budget_id : int
    budget_amount : int
    total_spent : int
    remaining_amt : int
    month : str

    @classmethod
    def from_db(cls, db_model: Budget):
        return cls (
            budget_id = db_model.budget_id,
            budget_amount = db_model.budget_amount,
            total_spent = db_model.total_spent, 
            remaining_amt = db_model.remaining_amt,
            month = db_model.month
        )
    
###### Business Logic Model (Pydantic)