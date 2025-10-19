class Task:

    def __init__(self, title, description, owner, id=None, status="Not Done"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.owner = owner




