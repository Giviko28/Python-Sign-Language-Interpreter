from customer import Customer
from book import Book

class Library:
    def __init__(self, customers: list[Customer], books: list[Book]):
        self.customers = customers
        self.books = books
    def RegisterCustomer(self, customer: Customer):
        if (customer not in self.customers and isinstance(customer, Customer)):
            self.customers.append(customer)
    def AddBook(self, book: Book):
        if (isinstance(book, Book)):
            self.books.append(book)
    def DisplayBooks(self):
        for book in self.books:
            if (book.status == "available"):
                print(book.author, " ", book.status)
    