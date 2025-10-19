import hashlib

class User:

    def __init__(self, userName, Email, password, id=None):
        self.id=id
        self.userName=userName
        self.Email=Email
        self.password=hashlib.sha256(password.encode()).hexdigest()
        self.tasks=[]

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.items.remove(task)
                print(f"task with ID {task_id} removed successfully.")
                return
        print(f"No task found with ID {task_id}.")
    def get_tasks(self):
        for task in self.tasks:
            print(f"task(id={task.id}, title='{task.title}', status={task.status})")
