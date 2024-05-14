class Customer:
    def __init__(self, name, age, borrowedBooks = []):
        self.name = name
        self.age = age
        self.borrowedBooks = list(borrowedBooks)
        
    def Borrow(self, book, customersList):
        if (book.status == "available"):
            book.status = "borrowed"
            self.borrowedBooks.append(book)
            if (self not in customersList):
                customersList.append(self)
    
    def Return(self, book, customersList):
        if (book in self.borrowedBooks):
            self.borrowedBooks.remove(book)
            book.status = "available"
            if (len(self.borrowedBooks) == 0):
                customersList.remove(self)
    
    
        
    