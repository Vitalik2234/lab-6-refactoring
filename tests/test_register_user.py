from models.user import User
from repositories.user_repository import UserRepository


def test_register_user():
    repo = UserRepository()
    user = User(1, "Taras")
    repo.add(user)
    assert repo.get_by_id(1).name == "Taras"


def test_register_multiple_users():
    repo = UserRepository()
    repo.add(User(1, "A"))
    repo.add(User(2, "B"))
    assert repo.get_by_id(2).name == "B"
