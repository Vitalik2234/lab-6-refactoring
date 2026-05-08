import pytest
from models.book import Book
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def env():
    br = BookRepository()
    ur = UserRepository()
    service = LibraryService(br, ur)
    br.add(Book(1, "Test", "A"))
    ur.add(User(1, "User"))
    service.issue_book(1, 1)
    return service


def test_return_success():
    service = env()
    book = service.return_book(1)
    assert book.is_issued is False


def test_return_twice():
    service = env()
    service.return_book(1)
    with pytest.raises(ValueError):
        service.return_book(1)


def test_return_nonexistent():
    service = env()
    with pytest.raises(ValueError):
        service.return_book(999)
