import json
from user import *
from book import Book


class Library:
    books = []
    users = []

    def __init__(
        self,
        LibraryName="",
        LibraryType="",
        LoanPeriod="",
        GracePeriod="",
        LoanExtensions="",
    ):
        self.LibraryName = LibraryName
        self.LibraryType = LibraryType
        self.LoanPeriod = LoanPeriod
        self.GracePeriod = GracePeriod
        self.LoanExtensions = LoanExtensions

    def data(self):
        with open("data.json", "r") as openfile:
            data = json.load(openfile)
            if data is not None:
                return data
            else:
                return dict()

    def get_users(self, dic, lists):
        if dic is not None:
            for data in dic:
                if data["type"] == "RegularUser":
                    lists.append(
                        RegularUser(
                            data["name"],
                            data["ID"],
                            data["email"],
                            data["paswd"],
                            data["socialSecurityNumber"],
                            data["address"],
                            data["creditCard"],
                        )
                    )

                elif data["type"] == "Student":
                    lists.append(
                        Student(
                            data["name"],
                            data["ID"],
                            data["email"],
                            data["paswd"],
                            data["socialSecurityNumber"],
                            data["address"],
                            data["creditCard"],
                        )
                    )

                elif data["type"] == "Librarian":
                    lists.append(
                        Librarian(
                            data["name"],
                            data["ID"],
                            data["email"],
                            data["paswd"],
                            data["socialSecurityNumber"],
                            data["address"],
                            data["creditCard"],
                        )
                    )

                elif data["type"] == "SystemAdmin":
                    lists.append(
                        SystemAdmin(
                            data["name"],
                            data["ID"],
                            data["email"],
                            data["paswd"],
                            data["socialSecurityNumber"],
                            data["address"],
                            data["creditCard"],
                        )
                    )

    def get_books(self, dicts, lists):
        if dicts is not None:
            for data in dicts:
                lists.append(
                    Book(
                        data["title"],
                        data["author"],
                        data["isbn"],
                        data["noOfCps"],
                        data["physOnl"],
                        data["loanPer"],
                        data["gracePer"],
                        data["extensionNum"],
                    )
                )

    def LookForUser(self, lst, name):
        for i, user in enumerate(lst):
            if user.name == name:
                return user

    def LookForBook(self, lst, title):
        for i, book in enumerate(lst):
            if book.title == title:
                return book

    def AuthenticateUser(self, name, password):
        user = self.LookForUser(self.users, name)
        try:
            if user.name == name and user.paswd == password:
                print(f"Welcome Back {name}")
                return True
        except:
            print("Please make sure you're registered.")
            return False

    def AddUser(
        self, name, ID, email, paswd, socialSecurityNumber, address, creditCard, lst
    ):
        privLev = int(
            input(
                "Chose the user type.\n 1.regular user, 2.student, 3.librarian, 4.admin"
            )
        )

        if privLev == 1:
            NewUser = RegularUser(
                name, ID, email, paswd, socialSecurityNumber, address, creditCard
            )

        elif privLev == 2:
            NewUser = Student(
                name, ID, email, paswd, socialSecurityNumber, address, creditCard
            )

        elif privLev == 3:
            NewUser = Librarian(
                name, ID, email, paswd, socialSecurityNumber, address, creditCard
            )

        elif privLev == 4:
            NewUser = SystemAdmin(
                name, ID, email, paswd, socialSecurityNumber, address, creditCard
            )

        lst.append(NewUser)

    def RemoveUser(self, registered: list):
        try:
            user = self.LookForUser(
                registered, input("enter the name of the user you want to remove")
            )
            registered.remove(user)
        except:
            print("The user you want to delete is not part of this library.")

    def AddBook(self, title, author, isbn, noOfCps, physOnl, bookLst):
        NewBook = Book(title, author, isbn, noOfCps, physOnl)
        bookLst.append(NewBook)
        return NewBook

    def RemoveBook(self, bookLst):
        try:
            book = self.LookForBook(
                bookLst, input("enter the title of the book you want to remove")
            )
            bookLst.remove(book)
        except:
            print("The book you want to delete is not in this library.")

    def RestrictUser(self, registered, restricted):
        try:
            user = self.LookForUser(
                registered, input("enter the name of the user you want to restrict")
            )
            restricted.append(user)
        except:
            print("user must be a part of the library to be banned")

    def BorrowingPolicy(self, bookLst, loanPer, gracePer, extensionNum):
        book = self.LookForBook(
            bookLst,
            input(
                "enter the title of the book you want to change the borrowing policy for"
            ),
        )
        try:
            book.loanPer = loanPer
            book.gracePer = gracePer
            book.extensionNum = extensionNum
        except:
            print("Book not found.")

    def BorrowBook(self, user, title, bookLst):
        try:
            book = self.LookForBook(bookLst, title)
            user.booksBorrowed.append(book)
            book.noOfCpsBorrowed += 1
            book.noOfCps -= 1
            self.activeLoans.append({title: user.name})
            book.__str__()
            print("book borrowed!")
        except:
            print("book unavailable.")

    def ReturnBook(self, user, title, bookLst, activeLoans: list):
        try:
            book = self.LookForBook(bookLst, title)
            user.booksBorrowed.remove(book)
            book.noOfCpsBorrowed -= 1
            book.noOfCps += 1
            activeLoans.remove({title: user.name})
        except:
            print("book unavailable.")