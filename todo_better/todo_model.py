import time

class Todo:
    def __init__(self, text="", completed=False, id=None):
        self.id = id if id else int(time.time() * 1000)  # Timestamp als ID
        self.text = text
        self.completed = completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data.get("text", ""),
            completed=data.get("completed", False),
            id=data.get("id")
        )