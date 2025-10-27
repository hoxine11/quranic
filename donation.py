class Donation:
    def __init__(self, donation_id, member_id, amount, date, note=None):
        self.id = donation_id
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.note = note
