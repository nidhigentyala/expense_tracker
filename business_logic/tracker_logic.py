from sqlalchemy.orm import Session
from dataacces.repository.expance_tracker import ExpenseTrackerRepo
from dataacces.repository.monthly_budget import BudgetTrackerRepo
from business_logic.models import ExpenseCreate,UpdateExpense,BudgetCreate
from dataacces.models import Expense,Budget

class ServicelayerOrBusinessLogic:
    def __init__(self, db_session:Session):
        self.db_session = db_session
        self.tracker_repo = ExpenseTrackerRepo(self.db_session)
        self.budget_repo = BudgetTrackerRepo(self.db_session)

    # create expenses
    async def create_new_expense(self, expense_create: ExpenseCreate):
        try:
            print(f"Request {expense_create}")
            create_new_expense = Expense(
                id = expense_create.id,
                title = expense_create.title,
                amount = expense_create.amount,
                category = expense_create.category,
                date = expense_create.date,
                user_id = expense_create.user_id,
                user_name = expense_create.user_name
            )
            db_result = self.tracker_repo.create_expese(create_new_expense)
            print(f"Check")
            print(f"DB Result is {ExpenseCreate.from_db(db_result)}")
            return ExpenseCreate.from_db(db_result)
        except Exception as e:
            print(f"{e}")
            print(f"Unable to init create exp with request {expense_create}")
    ## Complete the all te logical actions in this TODO

    # get all expenses 
    async def get_all_expenses(self):
            try:
                db_result = self.tracker_repo.get_expenses()
                expenses = []
                for expense in db_result :
                    expenses.append(ExpenseCreate.from_db(expense))
                return expenses
            except :
                print("Unable to get all expenses")

    # get expense by id
    async def get_expense_by_id(self,id:int):
            try:
                db_result = self.tracker_repo.get_expense_by_id(id)
                if db_result is None:
                    return None
                return ExpenseCreate.from_db(db_result)
            except :
                print(f"Unable to get expense by id {id}")
    # update expense 
    async def update_expense(self,expense_id: int,updated_expense: UpdateExpense):
            try :
                expense = self.tracker_repo.get_expense_by_id(expense_id)
                if expense is None:
                    return None
                expense.id = updated_expense.id
                expense.title = updated_expense.title
                expense.amount = updated_expense.amount
                expense.category = updated_expense.category
                expense.date = updated_expense.date
                expense.user_id = updated_expense.user_id
                expense.user_name = updated_expense.user_name
                db_result = self.tracker_repo.update_expense(expense_id,expense)
                return UpdateExpense.from_db(db_result)
            except Exception as e:
                print(f"{e}")

                print(f"Unable to update expense with id {expense_id}")

    # delete expense
    async def delete_expense(self,id:int):
            try :
                db_result = self.tracker_repo.delete_expense(id)
                if db_result is None :
                    return None
                return {"message":"Expense deleted successfully"}
            except :
                print(f"can't find expense with id {id}")

    # get expenses by category
    async def get_expenses_by_category(self, category: str):
            try :
                db_result = self.tracker_repo.get_expenses_by_category(category)
                if db_result is None :
                    return None
                expenses = []
                for expense in db_result :
                    expenses.append(ExpenseCreate.from_db(expense))
                return expenses
            except :
                print(f"Can't find the expense with category {category}")

    # get all expenses by date
    async def get_all_expenses_by_date(self,date : str) :
            try:
                db_result = self.tracker_repo.get_all_expenses_by_date(date)
                if not db_result :
                    return None
                print(f"DB Result is {[ExpenseCreate.from_db(expense) for expense in db_result]}")
                return [ExpenseCreate.from_db(expense) for expense in db_result]
            except :
                print(f"Can't find the expense with date {date}")

    # get all expenses by user id
    async def get_all_expenses_by_user_id(self,user_id : int):
            try :
                db_result = self.tracker_repo.get_all_expenses_by_user_id(user_id)
                if not db_result :
                    return None
                print(f"DB Result is {[ExpenseCreate.from_db(expense) for expense in db_result]}")
                return [ExpenseCreate.from_db(expense) for expense in db_result]
            except :
                print(f"Can't find expenses with user id {user_id}")