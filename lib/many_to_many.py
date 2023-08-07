class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [cont for cont in Contract.all if cont.author == self]

    def books(self):
        return [cont.book for cont in Contract.all if cont.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([cont.royalties for cont in Contract.all if cont.author == self])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [cont for cont in Contract.all if cont.book == self]

    def authors(self):
        return [cont.author for cont in Contract.all if cont.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls):
        sol = [cont for cont in cls.all]
        return sorted(sol, key=lambda cont: cont.date)