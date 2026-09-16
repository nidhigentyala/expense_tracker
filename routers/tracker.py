from fastapi import FastAPI, HTTPException, Depends, APIRouter
from typing import Annotated
from dataacces import models
from routers.models import ExpenseCreate, UpdateExpense, BudgetCreate, ExpenseCreateError
from config.session import engine, SessionLocal
from sqlalchemy.orm import Session
from config.session import get_db

from business_logic.tracker_logic import ServicelayerOrBusinessLogic

tracker_app = APIRouter()


# POST - Create Task
@tracker_app.post("/expenses")
async def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    try:
        print(f"Request at router level {expense}")
        service_logic = ServicelayerOrBusinessLogic(db_session=db)
        service_response = await service_logic.create_new_expense(expense)
        print(f"Response from the service layer is {service_response}")
        #return ExpenseCreate.model_dump(service_response)
        return service_response

    except Exception as e:
        print(f"Error creating expense : {e}")

        raise HTTPException(detail="Unable to create Expanse at the momemt", status_code=400)

# GET - Get all expenses
@tracker_app.get("/expenses")
async def get_all_expenses(db: Session = Depends(get_db)):
    try :
        service_logic = ServicelayerOrBusinessLogic(db_session=db)
        service_response = await service_logic.get_all_expenses()
        return service_response
    except Exception as e:
        print(f"Error fetching expense : {e}")
        raise HTTPException(detail="Unable to get all expenses at the moment", status_code=400)


# GET - Get expense by Id
@tracker_app.get("/expenses/{expense_id}")
async def get_expense_by_id(expense_id : int,db:Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.get_expense_by_id(expense_id)
    if service_response is None:
        raise HTTPException(detail="Expense not found", status_code=404)
    return service_response
    # #except Exception as e:
    #     print("Error",e)
    #     raise HTTPException(detail="Unable to get expense by ID at the moment", status_code=400)
    
# PUT - Update an expense
@tracker_app.put("/expenses/{expense_id}")
async def update_expense(expense_id: int, updated_expense: UpdateExpense, db: Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.update_expense(expense_id, updated_expense)
    if service_response is None:
        raise HTTPException(detail="Expense not found to Update", status_code=404)
    return service_response

# DELETE - Delete an expense
@tracker_app.delete("/expenses/{expense_id}")
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.delete_expense(expense_id)
    if service_response is None:
        raise HTTPException(detail="Expense not found to delete", status_code=404)
    return {"message": f"Expense with id {expense_id} deleted successfully"}

# GET - Get expenses by category
@tracker_app.get("/expenses/category/{category}")
async def get_expenses_by_category(category: str, db: Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.get_expenses_by_category(category)
    if not service_response:
        raise HTTPException(
            status_code=404,
            detail="Expenses not available with this category"
        )
    return service_response

# GET - Get all expenses on given date
@tracker_app.get("/expenses/date/{date}")
async def get_all_expenses_by_date(date: str, db: Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.get_all_expenses_by_date(date)
    if not service_response :
        raise HTTPException(
            status_code =404,
            detail = "Expenses not available with this date or Invalid date"
        )
    return service_response

# GET - Get all expenses by user id
@tracker_app.get("/expenses/user/{user_id}")
async def get_all_expenses_by_user_id(user_id: int, db: Session = Depends(get_db)):
    service_logic = ServicelayerOrBusinessLogic(db_session=db)
    service_response = await service_logic.get_all_expenses_by_user_id(user_id)
    if not service_response :
        raise HTTPException(
            status_code =404,
            detail = "Expenses not available with this user id or Invalid user id"
        )
    return service_response


## Health endpoint need to add TODO
@tracker_app.get("/health")
async def health():
    return {"status": "ok"}
