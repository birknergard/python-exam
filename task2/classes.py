
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title;
        self.author = author;
        self.num_pages = num_pages;
        self.available = True;

    def __str__(self):
        string_parts = [f"{self.title} written by {self.author}\n--> {self.num_pages} pages, "];
        if self.available: string_parts.append("Available");
        else: string_parts.append("Unavailable");

        return "".join(string_parts);


class Library:
    def __init__(self):
        self.books = [];

    def __str__(self):
        if len(self.books) == 0:
            return "Book list is empty\n";

        print("> List of Books <");
        book_list = []
        for i, book in enumerate(self.books):
            book_list.append(f"{i}. {str(book)}");
            if len(self.books) > 1:
                book_list.append("\n\n");

        return "".join(book_list);

    def add_book(self, book):
        self.books.append(book);

    def remove_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                self.books.pop(i);
                print(f"Book named {title} was deleted.");

    def check_out(self, title):
        for i, book in enumerate(self.books):

            if self.books[i].title == title: 
                if self.books[i].available == True:
                    self.books[i].available = False;
                else:
                    print("Book is already checked out");

    def check_in(self, title):
        for i, book in enumerate(self.books):

            if self.books[i].title == title:
                if self.books[i].available == False:
                    self.books[i].available = True;
                else:
                    print("Book is already checked in");








