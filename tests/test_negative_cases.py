import pytest
from models.book import Book
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def setup_env():
    br = BookRepository()
    ur = UserRepository()
    service = LibraryService(br, ur)
    br.add(Book(1, "A", "B"))
    ur.add(User(1, "Oleh"))
    return service


def test_issue_nonexistent_book():
    s = setup_env()
    with pytest.raises(ValueError):
        s.issue_book(99, 1)


def test_issue_nonexistent_user():
    s = setup_env()

    with pytest.raises(ValueError):
        s.issue_book(1, 999)


def test_issue_already_issued():
    s = setup_env()
    s.issue_book(1, 1)
    with pytest.raises(ValueError):
        s.issue_book(1, 1)


def test_return_not_issued():
    s = setup_env()
    with pytest.raises(ValueError):
        s.return_book(1)
