from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from models.book import Book
from models.user import User


class LibraryService:


    def __init__(self, book_repo: BookRepository, user_repo: UserRepository):

        self.book_repo = book_repo
        self.user_repo = user_repo

    def register_user(self, user: User) -> User:

        self.user_repo.add(user)
        return user

    def issue_book(self, book_id: int, user_id: int) -> Book:

        book = self.book_repo.get_by_id(book_id)
        if book is None:
            raise ValueError("Book not found")

        if book.is_issued:
            raise ValueError("Book already issued")

        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise ValueError("User not found")

        book.is_issued = True
        book.issued_to = user.id
        return book

    def return_book(self, book_id: int) -> Book:

        book = self.book_repo.get_by_id(book_id)
        if book is None:
            raise ValueError("Book not found")

        if not book.is_issued:
            raise ValueError("Book is not issued")

        book.is_issued = False
        book.issued_to = None
        return book

    def find_book_by_title(self, title: str):

        return self.book_repo.find_by_title(title)

