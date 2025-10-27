class Attendance:
    def __init__(self, session_id, member_id, status="present"):
        self.session_id = session_id
        self.member_id = member_id
        self.status = status  # present / absent / late
