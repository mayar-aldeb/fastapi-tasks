from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    name:str
    email:str
    password:str
class UserLogin(BaseModel):
    email: str
    password: str = Field(..., description="Your password", example="••••••")