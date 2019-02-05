from .. import usecases


class UserInMemoryRepository(usecases.UserRepository):
    def __init__(self):
        self.data = {}

    def list_user(self):
        return list(self.data.values())

    def find_user(self, user_id):
        return self.data.get(user_id)

    def upsert_user(self, user):
        self.data[user.id] = user

    def delete_user(self, user):
        self.data.pop(user.id, None)
