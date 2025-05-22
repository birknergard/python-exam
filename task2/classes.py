
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title;
        self.author = author;
        self.num_pages = num_pages;
        self.available = True;

class Library:
    def __init__(self):
        self.books = [];

    def add_book(self, book):
        self.books.append(book);

    def remove_book(self, title):
        for i in range(0, len(self.books)):
            if self.books[i].title == title:
                self.books.pop(i);
                print(f"Book named {title} was deleted.");

    def check_out(self, title):
        for i in range(0, len(self.books)):

            if self.books[i].title == title: 
                if self.books[i].available == True:
                    self.books[i].available = False;
                else:
                    print("Book is already checked out");

    def check_in(self, title):
        for i in range(0, len(self.books)):

            if self.books[i].title == title:
                if self.books[i].available == False:
                    self.books[i].available = True;
                else:
                    print("Book is already checked in");

    def print_books(self):
        print("> List of books <");
        if len(self.books) == 0:
            print("Book list is empty");
            return;

        for book in self.books:
            print(f"Title: {book.title} written by {book.author}\n--> {book.num_pages} pages");
            if book.available == True: print("--> Available\n");
            else: print("--> Unavailable\n");







