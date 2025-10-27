from user import User

class Instructor(User):
    def __init__(self, user_id, full_name, specialty, phone=None):
        super().__init__(user_id, full_name, phone)
        self.specialty = specialty  # tajwid / hifz / tilawah

    def get_role(self):
        return "Instructor"
