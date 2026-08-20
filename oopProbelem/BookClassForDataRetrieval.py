class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        print(f"Book Record: {self.title} | Author: {self.author} | ISBN : {self.isbn}")

x = Book("The C++ Programming Language", "Bjarne Stroustrup", "0321563840")
x.get_details()
