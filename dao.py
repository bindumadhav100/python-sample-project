
class UserDao:
    def __init__(self):
        self.mem_db = []

    def save(self, user):
        self.mem_db.append(user.__dict__)

    def get_all(self):
        return self.mem_db[:]