class Book:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Library:
    def __init__(self):
        self.__books = []  # Private

    def addBook(self, book_name):
        self.__books.append(book_name)

    def __iter__(self):
        return BookIterator(self.__books)

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index >= len(self.books):
            raise StopIteration

        return self.books[self.index]

library = Library()
library.addBook(Book("Huckleberry Finn"))
library.addBook(Book("Tom Sawyer"))
library.addBook(Book("Animal Farm"))
library.addBook(Book("Lord of the flies"))

for book in library:
    print (book)

###

# More efficient would be:
# class Library:
#     def __init__(self):
#         self.__books = []  # Private
#
#     def addBook(self, book_name):
#         self.__books.append(book_name)
#
#     def __iter__(self):
#         # Using a generator to yield books one by one
#         for book in self.__books:
#             yield book