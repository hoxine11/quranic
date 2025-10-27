from member import Member
from instructor import Instructor
from activity import Activity
from recomendation import Recommendation

m = Member(1, "Ahmed", 15, "M", quran_level="intermediate")
s = Instructor(2, "Sheikh Yassine", "Hifz")
a = Activity(10, "Hifz Circle A", "Hifz")

a.add_member(m)

print(m)  # Ahmed (Member)
print(s)  # Sheikh Yassine (Instructor)
print(a.title, "Members:", a.count_members())

rec = Recommendation()
print("Recommendation:", rec.generate(m))
