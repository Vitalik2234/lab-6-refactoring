from models.book import Book
from repositories.book_repository import BookRepository


def test_find_exact_title():
    repo = BookRepository()
    repo.add(Book(1, "Harry", "A"))
    results = repo.find_by_title("Harry")
    assert len(results) == 1


def test_find_case_insensitive():
    repo = BookRepository()
    repo.add(Book(1, "HARRY", "A"))
    assert len(repo.find_by_title("harry")) == 1


def test_find_empty_result():
    repo = BookRepository()
    repo.add(Book(1, "Book", "A"))
    assert repo.find_by_title("Nothing") == []
