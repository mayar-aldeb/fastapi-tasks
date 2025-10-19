# 🧠 FastAPI Task Management API

A clean, backend-only **Task Management API** built with **FastAPI** and **SQLite**, using full **OOP architecture** and **JWT authentication** for secure user access and task control.

---

## 🚀 Features

- User registration and login with **JWT authentication**  
- Each user can manage their own tasks securely  
- **CRUD operations** (Create, Read, Update, Delete) for tasks  
- Admin account with control over all users  
- Organized code structure using OOP (User, Task, Manager, DatabaseHandler)  
- Tested using **Swagger UI** and **Postman**  

---

## 🧩 Tech Stack

- **Python 3.12+**
- **FastAPI** – backend framework  
- **SQLite** – lightweight database  
- **hashlib** – password hashing  
- **JWT (PyJWT)** – secure authentication  
- **Pydantic** – data validation and serialization  

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/mayar-aldeb/fastapi-tasks.git

# 2. Navigate into the project
cd fastapi-tasks

# 3. (Optional) Create a virtual environment
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the FastAPI app
uvicorn main:app --reload
