from models.user import User


class UserRepository:


    def __init__(self):

        self.users = []

    def add(self, user: User) -> None:

        self.users.append(user)

    def get_by_id(self, user_id: int):

        return next((u for u in self.users if u.id == user_id), None)
