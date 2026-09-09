from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = "Expense_Tracker"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    date = Column(String)
    user_id = Column(Integer)
    user_name = Column(String)

class Budget(Base):
    __tablename__ = "Monthly_Budget"

    id = Column(Integer,primary_key =True, index = True)
    budget_amount = Column(Integer)
    total_spent = Column(Integer)
    remaining_amt = Column(Integer)
    month = Column(String)
    user_id = Column(Integer)
    user_name = Column(String)



##### DB Models (Sqlalchemy Models)