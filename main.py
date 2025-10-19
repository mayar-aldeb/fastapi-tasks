from fastapi import FastAPI
from routers import task_router,user_router

app=FastAPI()

@app.get("/")
def home():
    return {"message": "welcome"}


app.include_router(task_router.router)
app.include_router(user_router.router)










