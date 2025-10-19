from pydantic import BaseModel


class TaskBase(BaseModel):
    title:str
    description:str


class UpdateTask(BaseModel):
    task_id: int
    title: str
    description: str
