from user import *
from library import Library


class NationalLibrary(Library):
    # Class Variables
    registered = []
    restricted = []
    books = []
    activeLoans = []

    def __init__(
        self,
        LibraryName="National Library",
        LibraryType="National Library",
        LoanPeriod="",
        GracePeriod="",
        LoanExtensions="",
    ):
        super().__init__(
            LibraryName, LibraryType, LoanPeriod, GracePeriod, LoanExtensions
        )

    def get_users(self):
        if self.data():
            super().get_users(
                self.data()["nationalLibrary"]["registered"], self.registered
            )
            super().get_users(
                self.data()["nationalLibrary"]["restricted"], self.restricted
            )

    def get_books(self):
        if self.data():  # Returns False if dict is empty
            return super().get_books(
                self.data()["nationalLibrary"]["books"], self.books
            )

    def AddUser(self, user):
        if user.socialSecurityNumber is not None:
            self.registered.append(user)
            return True
        else:
            return False

    def BorrowBook(self, user):
        title = input("Enter the title of the book ou want to borrow ")
        if isinstance(user, RegularUser):
            if user.creditCard is not None:
                return super().BorrowBook(user, title, self.books)

    def AddBook(self, title, author, isbn, noOfCps, physOnl, bookLst):
        book = super().AddBook(title, author, isbn, noOfCps, physOnl, bookLst)
        super().books.append(book)
