class Activity:
    def __init__(self, activity_id, title, category, max_members=25):
        self.id = activity_id
        self.title = title
        self.category = category
        self.max_members = max_members
        self.members = []   # list of member IDs
        self.sessions = []  # list of Session objects

    def add_member(self, member):
        if len(self.members) < self.max_members and member.id not in self.members:
            self.members.append(member.id)

    def schedule_session(self, session):
        self.sessions.append(session)

    def count_members(self):
        return len(self.members)
    def display_summary(self):
        print(f"Activity: {self.title} ({self.category})")
        print(f"Max Members: {self.max_members} | Registered: {len(self.members)}")
        print("Members IDs:", self.members)
        print("-" * 30)
