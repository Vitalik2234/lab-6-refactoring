from controllers.library_controller import LibraryController
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def test_controller_register():
    br = BookRepository()
    ur = UserRepository()
    c = LibraryController(LibraryService(br, ur))

    c.register(User(10, "Test"))
    assert ur.get_by_id(10).name == "Test"
