from book import Book
from library import Library
from customer import Customer



customer1 = Customer("Givi", 15)
customer2 = Customer("Titiboy", 19)
customer3 = Customer("damn daniel", 21)


library = Library([], [])


library.AddBook(Book("Book", "Author of a Book", "31390123219031"))
library.AddBook(Book("Book2", "Author of a Book", "91931923129"))
library.AddBook(Book("Book2", "Author of a Book", "12312313131"))

library.RegisterCustomer(customer1)
library.RegisterCustomer(customer2)
library.RegisterCustomer(customer3)


library.customers[0].Borrow(library.books[1], library.customers)

library.DisplayBooks()
