class Book:
    def __init__(
        self,
        title,
        author,
        isbn,
        noOfCps=1,
        physOnl="",
        loanPer=0,
        gracePer=0,
        extensionNum=0,
    ):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._noOfCps = int(noOfCps)
        self.noOfCpsBorrowed = 0
        self._physOnl = physOnl
        self._loanPer = loanPer
        self._gracePer = gracePer
        self._extensionNum = extensionNum

    # Getters
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def noOfCps(self):
        return self._noOfCps

    @property
    def physOnl(self):
        return self._physOnl

    @property
    def loanPer(self):
        return self._loanPer

    @property
    def gracePer(self):
        return self._gracePer

    @property
    def extensionNum(self):
        return self._extensionNum

    # Setters
    @title.setter
    def title(self, title):
        self._title = title

    @author.setter
    def author(self, author):
        self._author = author

    @isbn.setter
    def email(self, email):
        self._email = email

    @noOfCps.setter
    def noOfCps(self, noOfCps):
        self._noOfCps = noOfCps

    @physOnl.setter
    def hysOnl(self, physOnl):
        self._physOnl = physOnl

    @loanPer.setter
    def loanPer(self, loanPer):
        self._loanPer = loanPer

    @gracePer.setter
    def gracePer(self, gracePer):
        self._gracePer = gracePer

    @extensionNum.setter
    def extensionNum(self, extensionNum):
        self._extensionNum = extensionNum

    def __dict__(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "noOfCps": self.noOfCps,
            "physOnl": self.physOnl,
            "loanPer": self.loanPer,
            "gracePer": self.gracePer,
            "extensionNum": self.extensionNum,
        }

    def __str__(self):
        return print(
            f"\ntitle:\t{self.title}"
            f"\nauthor:\t{self.author}"
            f"\nisbn:\t{self.isbn}"
            f"\ntotal copies:\t{self.noOfCps}"
        )
