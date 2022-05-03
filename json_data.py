import json
from library import Library
from school import SchoolLibrary
from municipal import MunicipalLibrary
from national import NationalLibrary

# Instances of libraries
library = Library()
schoolLibrary = SchoolLibrary()
municipalLibrary = MunicipalLibrary()
nationalLibrary = NationalLibrary()


def write_users(lst):
    data = []
    for user in lst:
        data.append(user.__dict__())
    return data


def write_books(lst):
    books = []
    for book in lst:
        books.append(book.__dict__())
    return books


def write_data():

    data_dict = {
        "libraryClass": {},
        "schoolLibrary": {},
        "municipalLibrary": {},
        "nationalLibrary": {},
    }

    data_dict["libraryClass"]["users"] = write_users(library.users)

    data_dict["schoolLibrary"]["registered"] = write_users(schoolLibrary.registered)
    data_dict["schoolLibrary"]["restricted"] = write_users(schoolLibrary.restricted)

    data_dict["municipalLibrary"]["registered"] = write_users(
        municipalLibrary.registered
    )
    data_dict["municipalLibrary"]["restricted"] = write_users(
        municipalLibrary.restricted
    )

    data_dict["nationalLibrary"]["registered"] = write_users(nationalLibrary.registered)
    data_dict["nationalLibrary"]["restricted"] = write_users(nationalLibrary.restricted)

    data_dict["libraryClass"]["books"] = write_books(library.books)
    data_dict["schoolLibrary"]["books"] = write_books(schoolLibrary.books)
    data_dict["municipalLibrary"]["books"] = write_books(municipalLibrary.books)
    data_dict["nationalLibrary"]["books"] = write_books(nationalLibrary.books)

    with open("data.json", "w") as f:
        json.dump(data_dict, f, indent=4)
