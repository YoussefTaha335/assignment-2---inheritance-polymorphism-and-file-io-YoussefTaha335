# Importing function from file
from json_data import *

# Importing all of the classes from files
from library import *
from school import SchoolLibrary
from municipal import MunicipalLibrary
from national import NationalLibrary

# Instances of libraries
library = Library()
schoolLibrary = SchoolLibrary()
municipalLibrary = MunicipalLibrary()
nationalLibrary = NationalLibrary()

# Importing data from json file using method from each library

# LIBRARY (SUPER CLASS)

data = library.data()  # RETURNS DICT
if data:
    library.get_users(data["libraryClass"]["users"], library.users)
    library.get_books(data["libraryClass"]["books"], library.books)

# SCHOOL LIBRARY (SUBCLASS)
schoolLibrary.get_users()
schoolLibrary.get_books()

# MUNICIPAL LIBRARY (SUBCLASS)
municipalLibrary.get_users()
municipalLibrary.get_books()

# NATIONAL LIBRARY (SUBCLASS)
nationalLibrary.get_users()
nationalLibrary.get_books()

# Welcome message to the user
print("HELLOOOOOOOOOOOOO!")

# Checking if the user already has an account
NewUser = input("Do you want to create a new account? (Yes/No)").lower()

# Creating new account
if NewUser == "yes":
    library.AddUser(
        input("name "),
        input("id "),
        input("email "),
        input("password "),
        input("Social Security Number (Optional) "),
        input("address (Optional) "),
        input("Credit Card (Optional) "),
        library.users,
    )
else:
    pass

# Asking the user for the username and password
name = input("Name: ")
password = input("Password: ")

# user variable
usr = library.LookForUser(library.users, name)

# Checking if the user has entered the right username and password
if library.AuthenticateUser(name, password):

    ####MENU####

    # Displaying the libraries for the regular user
    UsrInput = input("1) SCHOOL LIBRARY\t2) MUNICIPAL LIBRARY\t3) NATIONAL LIBRARY")

    if UsrInput == "1":
        userLibrary = schoolLibrary

    elif UsrInput == "2":
        userLibrary = municipalLibrary

    else:
        userLibrary = nationalLibrary

    while True:
        # Checking if the user is a Regular User or a Student
        if isinstance(usr, RegularUser) or isinstance(usr, Student):
            if userLibrary.AddUser(usr):
                userChoice = input(
                    "Dear user your options are:\n"
                    "1) Borrow a book\n"
                    "2) return a book\n"
                    "3) search for a book\n"
                    "4) EXIT\n"
                )

        # Checking if the user is a Librarian
        elif isinstance(usr, Librarian):
            if userLibrary.AddUser(usr):
                userChoice = input(
                    "\nDear Librarian your options are:\n"
                    "1) Add a book\n"
                    "2) Remove a book\n"
                    "3) Search for a book\n"
                    "4) change borrowing policy\n"
                    "5) EXIT\n"
                )

        # Checking if the user is a System Admin
        elif isinstance(usr, SystemAdmin):
            if userLibrary.AddUser(usr):
                userChoice = input(
                    "\nDear Admin your options are:\n"
                    "1) Add a user\n"
                    "2) Remove a user\n"
                    "3) Restrict user\n"
                    "4) EXIT\n"
                )

        # REGULAR USER AND STUDENT OPERATIONS
        if isinstance(usr, RegularUser) or isinstance(usr, Student):
            # borrow a book choice
            if int(userChoice) == 1:
                userLibrary.BorrowBook(usr)

            # return a book choice
            elif int(userChoice) == 2:
                title = input("Enter title of the book you want to borrow ")
                userLibrary.ReturnBook(usr, title, userLibrary.books)

            # search for a book choice
            elif int(userChoice) == 3:
                title = input("Enter title of the book you're looking for")
                book = userLibrary.LookForBook(userLibrary.books, title)
                book.__str__()

            elif int(userChoice) == 4:
                break

        # LIBRARIAN OPERATIONS
        elif isinstance(usr, Librarian):
            # Add a book choice
            if int(userChoice) == 1:
                userLibrary.AddBook(
                    input("title: "),
                    input("author: "),
                    input("isbn"),
                    input("Total Copies: "),
                    input("Physical or Online: "),
                    userLibrary.books,
                )

            # Remove a book choice
            elif int(userChoice) == 2:
                userLibrary.RemoveBook(userLibrary.books)

            # search for a book choice
            elif int(userChoice) == 3:
                title = input("Enter title of the book you're looking for")
                book = userLibrary.LookForBook(userLibrary.books, title)
                book.__str__()

            elif int(userChoice) == 4:
                break

        # SYSTEM ADMIN OPERATIONS
        elif isinstance(usr, SystemAdmin):
            # add user to the list
            if int(userChoice) == 1:
                userLibrary.AddUser(usr)

            # remove user to the list
            elif int(userChoice) == 2:
                userLibrary.RemoveUser(userLibrary.registered)

            elif int(userChoice) == 3:
                break

write_data()    # Function that saves ALL of the data to JSON file
