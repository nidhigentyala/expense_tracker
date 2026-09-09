from fastapi import FastAPI
from routers.tracker import tracker_app
from routers.budget import budget_app

app=FastAPI(title="Personal Expense Tracker")

app.include_router(tracker_app, prefix="/tracker", tags=["Tracker"])
app.include_router(budget_app, prefix="/budget", tags=["Budget"])

# app.mount("/budget", budget_app)

# app.mount("/tracker", tracker_app)





