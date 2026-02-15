class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author
        self.is_borrowed = False
        
    def display_info(self):
        status ="Available" if not self.is_borrowed else "Borrowed"
        print(f"Title : '{self.title}' ")
        print(f"Author: '{self.author}' ")
        print(f"Status: '{status}' ")
class Library:
    def __init__(self):
        self.books=[]
        
    def add_book(self, title, author):
        new_book=Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
        
    def view_books(self):
        if not self.books:
            print("NO books in the library.")
        else:
            print("----Library Catalog---\n")
            for book in self.books:
                book.display_info()
                
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed =True
                print(f"Book '{title}' has been borrowed.")
                return
        print(f"Book '{title}' is not available for borrowing.")

