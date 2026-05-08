from models.book import Book


class BookRepository:


    def __init__(self):

        self.books = []

    def add(self, book: Book) -> None:

        self.books.append(book)

    def get_by_id(self, book_id: int):

        return next((b for b in self.books if b.id == book_id), None)

    def find_by_title(self, title: str):

        return [b for b in self.books if b.title.lower() == title.lower()]
