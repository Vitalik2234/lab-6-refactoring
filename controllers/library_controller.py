from dto.book_dto import IssueBookDTO
from models.user import User
from services.library_service import LibraryService


class LibraryController:


    def __init__(self, library_service: LibraryService):

        self.service = library_service

    def issue(self, dto: IssueBookDTO):

        return self.service.issue_book(dto.book_id, dto.user_id)

    def return_book(self, book_id: int):

        return self.service.return_book(book_id)

    def find_book(self, title: str):

        return self.service.find_book_by_title(title)

    def register(self, user: User):

        return self.service.register_user(user)
