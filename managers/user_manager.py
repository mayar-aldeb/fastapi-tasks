import hashlib
from models.User import User




class UserManager:
    def __init__(self, db_handler):
        self.db_handler = db_handler  # use existing DB connection

    def register_user(self, user:User):
        return(self.db_handler.add_user(user))

    def login_user(self,email, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        row = self.db_handler.check_email(email, password)
        if row:
            user = User(row[1], row[2], row[3], row[0])
            print("log in successfully")
            return user
        else:
            print("invalid email or password")
            return None

    def get_user_by_email(self, email):
        row=self.db_handler.get_user_by_email(email)

        if row:
            user = User(row[1], row[2], row[3], row[0])
            return user
        else:
            print("invalid email")
            return None

    def get_all_users(self):
        rows=self.db_handler.get_all_users()
        users=[]
        if rows:
            for row in rows:
                user = User(row[1], row[2], row[3], row[0])
                users.append(user)
                print(row)
        else:
            print("no users submitted yet")
        return users

    def delete_user(self,user_id):
        self.db_handler.delete_user(user_id)
        print("✅ user deleted successfully.")

