import csv
from member import Member
from activity import Activity

def load_members(filename="members.csv"):
    members = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            m = Member(
                user_id=int(row["id"]),
                full_name=row["full_name"],
                age=int(row["age"]),
                gender=row["gender"],
                phone=row["phone"],
                address=row["address"],
                quran_level=row["quran_level"]
            )
            members.append(m)
    return members


def load_activities(filename="activities.csv"):
    activities = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = Activity(
                activity_id=int(row["id"]),
                title=row["title"],
                category=row["category"],
                max_members=int(row["max_members"])
            )
            activities.append(a)
    return activities
