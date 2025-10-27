from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, full_name, phone=None):
        self.id = user_id
        self.full_name = full_name
        self.phone = phone

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.full_name} ({self.get_role()})"
