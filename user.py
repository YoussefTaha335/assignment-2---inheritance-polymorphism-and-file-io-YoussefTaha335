class User:
    def __init__(
        self,
        name="",
        ID="",
        email="",
        paswd="",
        socialSecurityNumber="",
        address="",
        creditCard="",
    ):
        self._name = name
        self._ID = ID
        self._email = email
        self._paswd = paswd
        self._socialSecurityNumber = socialSecurityNumber
        self._address = address
        self._creditCard = creditCard
        self.booksBorrowed = list()

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def ID(self):
        return self._ID

    @property
    def email(self):
        return self._email

    @property
    def paswd(self):
        return self._paswd

    @property
    def socialSecurityNumber(self):
        return self._socialSecurityNumber

    @property
    def address(self):
        return self._address

    @property
    def creditCard(self):
        return self._paswd

    # Setters
    @name.setter
    def name(self, name):
        self._name = name

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @email.setter
    def email(self, email):
        self._email = email

    @paswd.setter
    def paswd(self, paswd):
        self._paswd = paswd

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber):
        self._socialSecurityNumber = socialSecurityNumber

    @address.setter
    def address(self, address):
        self._address = address

    @creditCard.setter
    def creditCard(self, creditCard):
        self._creditCard = creditCard

    def __dict__(self):
        return {
            "name": self.name,
            "ID": self.ID,
            "email": self.email,
            "paswd": self.paswd,
            "socialSecurityNumber": self.socialSecurityNumber,
            "address": self.address,
            "creditCard": self.creditCard,
            "type": self.__class__.__name__,
        }


class RegularUser(User):
    def __init__(
        self, name, ID, email, password, socialSecurityNumber, address, creditCard
    ):
        super().__init__(
            name, ID, email, password, socialSecurityNumber, address, creditCard
        )

    def __dict__(self):
        return super().__dict__()


class Student(User):
    def __init__(
        self, name, ID, email, password, socialSecurityNumber, address, creditCard
    ):
        super().__init__(
            name, ID, email, password, socialSecurityNumber, address, creditCard
        )

    def __dict__(self):
        return super().__dict__()


class Librarian(User):
    def __init__(
        self, name, ID, email, paswd, socialSecurityNumber, address, creditCard
    ):
        super().__init__(
            name, ID, email, paswd, socialSecurityNumber, address, creditCard
        )

    def __dict__(self):
        return super().__dict__()


class SystemAdmin(User):
    def __init__(
        self, name, ID, email, paswd, socialSecurityNumber, address, creditCard
    ):
        super().__init__(
            name, ID, email, paswd, socialSecurityNumber, address, creditCard
        )

    def __dict__(self):
        return super().__dict__()
