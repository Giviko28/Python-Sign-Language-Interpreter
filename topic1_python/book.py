class Book:
    def __init__(self, title, author, ISBN, status = "available"):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status
    
    def Borrow(self):
        if(self.status == "borrowed"):
            print("womp womp book is already borrowed")
            return
        self.status = "borrowed"
    
    def Return(self):
        if(self.status == "available"):
            print("cant return a book you dont have bro")
            return
        self.status = "available"
    
    
