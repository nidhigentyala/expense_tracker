from sqlalchemy.orm import Session
from dataacces.models import Expense, Budget

class ExpenseTrackerRepo :
    def __init__(self,db_session : Session):
        self.db = db_session
        
    def create_expese(self,expense: Expense) -> Expense:
        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense

    def get_expenses(self) :
        return self.db.query(Expense).all()

    def get_expense_by_id(self,id : int):
        return self.db.query(Expense).filter(Expense.id == id).first()

    def update_expense(self,expense_id: int,updated_expense: Expense):
        expense = self.db.query(Expense).filter(Expense.id == expense_id).first()

        if expense is None:
            return None
        self.db.add(updated_expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense

    def delete_expense(self,id :int):
        expense = self.db.query(Expense).filter(Expense.id == id).first()
        if expense is None:
            return None
        self.db.delete(expense)
        self.db.commit()
        return expense

    def get_expenses_by_category(self, category: str):
        category = category.lower().strip()
        return self.db.query(Expense).filter(Expense.category.ilike(category)).all()

    def get_all_expenses_by_date(self,date : str) :
        return self.db.query(Expense).filter(Expense.date == date).all()    

    def get_all_expenses_by_user_id(self,user_id :int):
        return self.db.query(Expense).filter(Expense.user_id == user_id).all()