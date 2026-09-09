from fastapi import FastAPI


from routers.tracker import tracker_app
from routers.budget import budget_app

app=FastAPI(title="Personal Expense Tracker")

app.mount("/budget", budget_app)

app.mount("/tracker", tracker_app)


## Health endpoint need to add TODO
