from pydantic import BaseModel

from dataacces.models import Expense,Budget


class ExpenseCreate(BaseModel):
    title: str
    amount: int
    category: str
    date: str
    user_id: int
    user_name: str

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            id = db_model.id,
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date,
            user_id = db_model.user_id,
            user_name = db_model.user_name
        )

class UpdateExpense(ExpenseCreate):
    id : int
    title: str
    amount: int
    category: str 
    date: str 
    user_id: int
    user_name: str

    @classmethod
    def from_db(cls, db_model: Expense):
        return cls(
            id = db_model.id,
            title = db_model.title,
            amount = db_model.amount,
            category = db_model.category,
            date = db_model.date,
            user_id = db_model.user_id,
            user_name = db_model.user_name
        )
    

class BudgetCreate(BaseModel):
    budget_amount : int
    total_spent : int
    remaining_amt : int
    month : str
    user_id: int
    user_name: str

    @classmethod
    def from_db(cls, db_model: Budget):
        return cls (
            budget_id = db_model.budget_id,
            budget_amount = db_model.budget_amount,
            total_spent = db_model.total_spent, 
            remaining_amt = db_model.remaining_amt,
            month = db_model.month,
            user_id = db_model.user_id,
            user_name = db_model.user_name
        )
    
###### Business Logic Model (Pydantic)