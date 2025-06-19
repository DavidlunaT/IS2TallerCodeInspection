class Task:
    def __init__(self, title, tags=None):
        self.title = title
        self.status = "pending"
        self.tags = tags if tags is not None else []

    def complete(self):
        self.status = "done"

    def __str__(self):
        return f"{self.title} is {self.status}"
