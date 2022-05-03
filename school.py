from user import *
from library import Library


class SchoolLibrary(Library):
    # Class Variables
    registered = []
    restricted = []
    books = []
    activeLoans = []

    def __init__(
        self,
        LibraryName="School Library",
        LibraryType="School Library",
        UsersAllowed=["student", "librarian", "system admin"],
        LoanPeriod="",
        GracePeriod="",
        LoanExtensions="",
    ):
        super().__init__(
            LibraryName, LibraryType, LoanPeriod, GracePeriod, LoanExtensions
        )
        self.UsersAllowed = UsersAllowed

    def get_users(self):
        if self.data():  # Returns False if dict is empty
            super().get_users(
                self.data()["schoolLibrary"]["registered"], self.registered
            )
            super().get_users(
                self.data()["schoolLibrary"]["restricted"], self.restricted
            )

    def get_books(self):
        if self.data():  # Returns False if dict is empty
            return super().get_books(self.data()["schoolLibrary"]["books"], self.books)

    def AddUser(self, user):
        if (
            isinstance(user, Student)
            or isinstance(user, Librarian)
            or isinstance(user, SystemAdmin)
        ):
            self.registered.append(user)
            return True
        else:
            return False

    def BorrowBook(self, user):
        title = input("Enter the title of the book ou want to borrow ")
        if isinstance(user, Student):
            return super().BorrowBook(user, title, self.books)

    def AddBook(self, title, author, isbn, noOfCps, physOnl, bookLst):
        book = super().AddBook(title, author, isbn, noOfCps, physOnl, bookLst)
        super().books.append(book)
