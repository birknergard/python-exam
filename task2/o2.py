import classes 

# MAIN PROGRAM
library = classes.Library();

book_one = classes.Book("The Bible", "Various authors", 2000);
book_two = classes.Book("Game of Thrones", "GRRM", 700);

print("1. Adding books ...");
library.add_book(book_one);
library.add_book(book_two);
library.print_books();

print("2. Checkin in already checked in book ...");
library.check_in("The Bible");


print("3. Checking out book ...");
library.check_out("The Bible");
library.print_books();

print("4. Checking out already checked out book ...");
library.check_out("The Bible");

print("5. Checking in book ...");
library.check_in("The Bible");
library.print_books();

print("6. Removing book from library ...");
library.remove_book("Game of Thrones");
library.print_books();
# END
