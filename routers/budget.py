from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from dataacces import models
from routers.models import ExpenseCreate, UpdateExpense, BudgetCreate, ExpenseCreateError
from config.session import engine, SessionLocal
from sqlalchemy.orm import Session
from config.session import get_db

from business_logic.tracker_logic import ServicelayerOrBusinessLogic
from business_logic.budget_logic import BudgetBusinessLogic

budget_app = FastAPI(title="Personal Expense Tracker")


# POST - Create Budget
@budget_app.post("/budget")
async def create_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    try:
        print(f"Request at router level {budget}")
        service_logic = BudgetBusinessLogic(db_session=db)
        service_response = await service_logic.create_new_budget(budget)
        print(f"Response from the service layer is {service_response}")
        return BudgetCreate.model_dump(service_response)
        # return service_response

    except Exception as e:
        print(f"str{e}")

        raise HTTPException(detail="Unable to create Budget at the momemt", status_code=400)

# GET - Get Budget Status
@budget_app.get("/status")
async def get_budget_status(db: Session = Depends(get_db)):
    try:
        service_logic = BudgetBusinessLogic(db_session=db)
        service_response = await service_logic.budget_status()
        print(f"Response from the service layer is {service_response}")
        if service_response is None:
            raise HTTPException(detail="No budget found", status_code=404)
        return service_response
    except HTTPException:
        raise
    except Exception as e:
        print(f"str{e}")
        raise HTTPException(detail="Unable to get budget status at the moment", status_code=400)

# GET - Get Budget by id
@budget_app.get("/budget/{budget_id}")
async def get_budget_by_id(budget_id:int, db:Session = Depends(get_db)):
    try :
        service_logic = BudgetBusinessLogic(db_session = db)
        service_response = await service_logic.get_budget_by_id(budget_id)
        if service_response is None:
            raise HTTPException(detail="Budget not found for this id", status_code=404)
        return service_response
    except HTTPException:
        raise
    except Exception as e:
        print(f"str{e}")
        raise HTTPException(detail="Unable to get budget by id at the moment", status_code=400)

# GET - Get Budget by user id
@budget_app.get("/budget/user/{user_id}")
async def get_budget_by_user_id(user_id:int, db:Session = Depends(get_db)):
    try :
        service_logic = BudgetBusinessLogic(db_session = db)
        service_response = await service_logic.get_budget_by_user_id(user_id)
        if service_response is None:
            raise HTTPException(detail="Budget not found for this user id", status_code=404)
        return service_response
    except HTTPException:
        raise
    except Exception as e:
        print(f"str{e}")
        raise HTTPException(detail="Unable to get budget by user id at the moment", status_code=400)