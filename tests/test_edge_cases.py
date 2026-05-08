import pytest
from models.book import Book
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def test_issue_missing_user_and_book():
    service = LibraryService(BookRepository(), UserRepository())
    with pytest.raises(ValueError):
        service.issue_book(1, 1)


def test_service_with_empty_repos():
    service = LibraryService(BookRepository(), UserRepository())
    assert service.find_book_by_title("Any") == []
