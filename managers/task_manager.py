from models.Task import Task


class TaskManager:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_task(self, user_id, task):
        self.db_handler.insert_task(user_id, task)
        print("✅ Task added successfully.")

    def get_user_tasks(self, user_id):

        rows=self.db_handler.get_tasks_by_user(user_id)
        tasks=[]
        if rows:
            for row in rows:
                print(row[:-1])
                task=Task(row[1],row[2],row[4],row[0],row[3])
                tasks.append(task)
        else:
            print("no tasks submitted yet")
        return tasks

    def update_task(self, task_id, title,description,user_id):
        r=self.db_handler.update_task_details(task_id, title, description,user_id)
        if r==0:
            print("no tasks with this id")
        else:
            print("✅ Task updated successfully.")
        return r

    def update_status(self,task_id,status,user_id):
        r=self.db_handler.update_task_status(task_id,status,user_id)
        if r==0:
            print("no tasks with this id")
        else:
            print("✅ status updated successfully.")
        return r

    def delete_task(self, task_id,user_id):
        r=self.db_handler.delete_task(task_id,user_id)
        if r==0:
            print("no tasks with this id")
        else:
            print("✅ task deleted successfully.")
        return r
