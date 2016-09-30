
class UserDao:
    def __init__(self):
        self.mem_db = []

    def save(self, user):
        self.mem_db.append(user.__dict__)
        for i, saved_user in enumerate(self.mem_db):
            saved_user['id'] = i

    def get_all(self):
        return self.mem_db[:]
        
    def get_by_id(self, id):
        for user in self.mem_db:
            print(user)
            if user['id'] == id:
                return user
        return {}