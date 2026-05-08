import pytest
from controllers.library_controller import LibraryController
from dto.book_dto import IssueBookDTO
from models.book import Book
from models.user import User
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from services.library_service import LibraryService


def make_controller():
    br = BookRepository()
    ur = UserRepository()
    br.add(Book(1, "A", "B"))
    ur.add(User(1, "X"))
    service = LibraryService(br, ur)
    return LibraryController(service)


def test_controller_issue_success():
    c = make_controller()
    dto = IssueBookDTO(1, 1)
    book = c.issue(dto)
    assert book.is_issued is True


def test_controller_issue_invalid_dto():
    c = make_controller()
    with pytest.raises(AttributeError):
        c.issue("wrong")


def test_controller_issue_nonexistent():
    c = make_controller()
    dto = IssueBookDTO(99, 1)
    with pytest.raises(ValueError):
        c.issue(dto)
