from fastapi import APIRouter,Depends,HTTPException
from managers.task_manager import TaskManager
from models.Task import Task
from schemas import task_schema
from database.DatabaseHandler import DatabaseHandler
from security import auth_handler
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

auth_scheme = HTTPBearer()


db = DatabaseHandler("app.db")
manager = TaskManager(db)
router=APIRouter(prefix="/tasks",tags=["Tasks"])



@router.post("/insert_task")
def insert_task(task_data: task_schema.TaskBase,token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    task=Task(task_data.title,task_data.description,user_id)
    manager.add_task(user_id, task)
    return {"message": " task added successfully."}


@router.get("/get_tasks")
def get_tasks(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    tasks=manager.get_user_tasks(user_id)
    return {"tasks":tasks}




@router.put("/update task")
def update_task(task_data:task_schema.UpdateTask,token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    r=manager.update_task(task_data.task_id,task_data.title,task_data.description,user_id)
    if r == 0:
        return {"message": " no tasks with this id"}
    else:
        return {"message": " task updated successfully."}



@router.put("/update status")
def update_status(task_id: int, status: str,token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    r=manager.update_status(task_id, status,user_id)
    if r == 0:
        return {"message": " no tasks with this id"}
    else:
        return {"message": " status updated successfully."}


@router.delete("/delete task")
def delete_task(task_id:int,token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    r=manager.delete_task(task_id,user_id)
    if r == 0:
        return {"message": " no tasks with this id"}
    else:
        return {"message": " task deleted successfully."}

