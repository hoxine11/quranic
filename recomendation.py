class Recommendation:
    def generate(self, member):
        if member.quran_level == "beginner":
            return "Halaqat Tilawah (Circle of Recitation)"
        elif member.quran_level == "intermediate":
            return "Halaqat Hifz (Memorization Circle)"
        elif member.quran_level == "hafiz":
            return "Assistant Teacher / Revision Leader"
        return "General Group Participation"
