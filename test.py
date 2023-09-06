class BandObj:
    def __init__(self):
        self.members = []

    def add_member(self, *member):
        self.members.extend(member)


