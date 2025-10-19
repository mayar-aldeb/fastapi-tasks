from fastapi import APIRouter,Depends,HTTPException
from managers.user_manager import UserManager
from models.User import User
from schemas import user_schema
from database.DatabaseHandler import DatabaseHandler
from security import auth_handler
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

auth_scheme = HTTPBearer()


router = APIRouter(prefix="/users",tags=["Users"])
db = DatabaseHandler("app.db")
manager = UserManager(db)


@router.post("/register")
def register(user_data:user_schema.UserBase):
    user=User(user_data.name,user_data.email,user_data.password)
    reg=manager.register_user(user)
    if reg==1:
        return {"message": " User added successfully."}

    else:
        return {"message": " Error: Email already exists."}


@router.post("/log_in")
def log_in(user_data:user_schema.UserLogin):
    user=manager.login_user(user_data.email,user_data.password)
    role = "admin" if user.Email == "mayar.aldeb8@gmail.com" else "user"
    token = auth_handler.create_access_token({"user_id": user.id,"email": user.Email,"role": role})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/get by email")
def get_user_by_email(email: str,token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    user=manager.get_user_by_email(email)
    if user:
        return {"message": "got mail successful", "user name": user.userName}
    else:
        return {"message": "invalid email"}


@router.get("/get all users")
def get_all_users(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    users=manager.get_all_users()
    if users:
        usernames = [user.userName for user in users]
        return {"message": "got mails successful", "user name": usernames}
    else:
        print("no users submitted yet")


@router.delete("/delete user")
def delete_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    payload = auth_handler.verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload["user_id"]
    manager.delete_user(user_id)
    return {"message": "user deleted successfully"}
