class Book:


    def __init__(self, book_id: int, title: str, author: str):

        self.id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.issued_to = None
