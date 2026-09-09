from sqlalchemy.orm import Session
from dataacces.repository.expance_tracker import ExpenseTrackerRepo
from dataacces.repository.monthly_budget import BudgetTrackerRepo
from business_logic.models import ExpenseCreate,BudgetCreate
from dataacces.models import Expense,Budget

class BudgetBusinessLogic:
    def __init__(self, db_session:Session):
        self.db_session = db_session
        self.tracker_repo = ExpenseTrackerRepo(self.db_session)
        self.budget_repo = BudgetTrackerRepo(self.db_session)

    async def create_new_budget(self, budget_create: BudgetCreate):
                try:
                    print(f"Request {budget_create}")
                    create_new_budget= Budget(
                        budget_amount = budget_create.budget_amount,
                        total_spent = budget_create.total_spent,
                        remaining_amt = budget_create.remaining_amt,
                        month = budget_create.month,
                        user_id = budget_create.user_id,
                        user_name = budget_create.user_name
                    )
                    db_result = self.budget_repo.create_monthly_budget(create_new_budget)
                    print(f"Check")
                    print(f"DB Result is {BudgetCreate.from_db(db_result)}")
                    return BudgetCreate.from_db(db_result)
                except Exception as e:
                    print(f"{e}")
                    print(f"Unable to init create exp with request {budget_create}")

    async def budget_status(self) :
                try :
                    db_result = self.budget_repo.budget_status()
                    if db_result is None:
                        return None
                    return db_result
                except :    
                    print(f"Unable to get budget status")

    async def get_budget_by_id(self, id :int):
                try :
                    db_result = self.budget_repo.get_budget_by_id(id)
                    if not db_result:
                        return None
                    print(f"DB Result is {BudgetCreate.from_db(db_result)}")
                    return BudgetCreate.from_db(db_result)
                except :
                    print(f"Unable to get budget by id {id}")

    async def get_budget_by_user_id(self, user_id :int):
                try :
                    db_result = self.budget_repo.get_budget_by_user_id(user_id)
                    if not db_result:
                        return None
                    # print(f"DB Result is {BudgetCreate.from_db(db_result)}")
                    # return [BudgetCreate.from_db(db_result) for budget in db_result]
                    budgets = []
                    for budget in db_result :
                        budgets.append(BudgetCreate.from_db(budget))
                    return budgets
                except :
                    print(f"Unable to get budget by user id {user_id}")
