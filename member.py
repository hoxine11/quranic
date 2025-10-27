from user import User

class Member(User):
    def __init__(self, user_id, full_name, age, gender, phone=None, address=None,
                 guardian_name=None, guardian_phone=None, quran_level="beginner"):
        super().__init__(user_id, full_name, phone)
        self.age = age
        self.gender = gender
        self.address = address
        self.guardian_name = guardian_name
        self.guardian_phone = guardian_phone
        self.quran_level = quran_level
        self.activities = []  # list of activity IDs

    def register_for(self, activity):
        if activity.id not in self.activities:
            self.activities.append(activity.id)

    def get_role(self):
        return "Member"
    def display_info(self):
        print(f"[{self.get_role()}] {self.full_name}")
        print(f"Age: {self.age} | Level: {self.quran_level}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print("-" * 30)
