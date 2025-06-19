class Task:
    def __init__(self, title, tags=[]):  # ❌ BUG: mutable default argument
        self.title = title
        self.status = "pending"
        self.tags = tags

    def complete(self):
        self.status = "done"

    def __str__(self):
        return f"{self.title} is {self.status}"
