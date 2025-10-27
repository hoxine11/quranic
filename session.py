class Session:
    def __init__(self, session_id, activity_id, instructor_id, date, start_time, end_time, location):
        self.id = session_id
        self.activity_id = activity_id
        self.instructor_id = instructor_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.attendance = []  # list of Attendance

    def add_attendance(self, attendance):
        self.attendance.append(attendance)
