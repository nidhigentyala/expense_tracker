from sqlalchemy.orm import Session
from dataacces.models import Expense, Budget

class BudgetTrackerRepo :
    def __init__(self,db_session : Session):
        self.db = db_session


    def create_monthly_budget(self,budget: Budget) -> Budget:
        self.db.add(budget)
        self.db.commit()
        self.db.refresh(budget)
        return budget

    def budget_status(self):
        budgets = self.db.query(Budget).all()
        if not budgets:
            return None
        results = []
        for budget in budgets:
            if budget.total_spent > budget.budget_amount:
                results.append(
                    {
                        "id": budget.id,
                        "budget_amount": budget.budget_amount,
                        "total_spent": budget.total_spent,
                        "remaining_amt": budget.remaining_amt,
                        "month": budget.month,
                        "warning": "Spent more than Budget"
                    }
                )
            else:
                results.append(
                    {
                        "id": budget.id,
                        "budget_amount": budget.budget_amount,
                        "total_spent": budget.total_spent,
                        "remaining_amt": budget.remaining_amt,
                        "month": budget.month,
                        "status": "OK"
                    }
                )
        return results

    def delete_budget(self,id :int):
            budget = self.db.query(Budget).filter(Budget.id == id).first()
            if budget is None:
                return None
            self.db.delete(budget)
            self.db.commit()
            return budget

    def get_budget_by_id(self,id : int):
        return self.db.query(Budget).filter(Budget.id == id).first()

    def get_budget_by_user_id(self,user_id : int):
        return self.db.query(Budget).filter(Budget.user_id == user_id).all()    
    