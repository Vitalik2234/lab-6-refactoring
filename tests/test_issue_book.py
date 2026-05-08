import pytest
from models.book import Book
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def create_env():
    book_repo = BookRepository()
    user_repo = UserRepository()
    service = LibraryService(book_repo, user_repo)

    book_repo.add(Book(1, "HP1", "Rowling"))
    book_repo.add(Book(2, "HP2", "Rowling"))
    user_repo.add(User(1, "Ivan"))
    user_repo.add(User(2, "Anna"))

    return service


def test_issue_success():
    service = create_env()
    book = service.issue_book(1, 1)
    assert book.is_issued is True
    assert book.issued_to == 1


def test_issue_multiple_books():
    service = create_env()
    service.issue_book(1, 1)
    book2 = service.issue_book(2, 2)
    assert book2.is_issued is True


def test_issue_by_same_user():
    service = create_env()
    service.issue_book(1, 1)
    service.issue_book(2, 1)
    assert service.book_repo.get_by_id(2).issued_to == 1


def test_issue_book_id_type_error():
    service = create_env()
    with pytest.raises(ValueError):
        service.issue_book("abc", 1)
