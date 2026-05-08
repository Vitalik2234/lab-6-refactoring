from models.book import Book
from repositories.book_repository import BookRepository


def test_repo_add_books():
    repo = BookRepository()
    repo.add(Book(1, "A", "B"))
    repo.add(Book(2, "C", "D"))
    assert len(repo.books) == 2


def test_repo_get_by_id_none():
    repo = BookRepository()
    assert repo.get_by_id(123) is None


def test_repo_duplicate_ids():
    repo = BookRepository()
    repo.add(Book(1, "A", "B"))
    repo.add(Book(1, "C", "D"))
    assert len([b for b in repo.books if b.id == 1]) == 2
