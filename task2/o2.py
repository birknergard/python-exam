import classes 

# MAIN PROGRAM
library = classes.Library();

book_one = classes.Book("The Bible", "Various authors", 2000);
book_two = classes.Book("Game of Thrones", "GRRM", 700);

print("1. Adding books ...");
library.add_book(book_one);
library.add_book(book_two);
library.add_book(classes.Book("Eragon", "Christopher Paolini", 600));
print(library);

print("\n2. Checkin in already checked in book ...");
library.check_in("The Bible");

print("\n3. Checking out book ...");
library.check_out("The Bible");
print(library);

print("\n4. Checking out already checked out book ...");
library.check_out("The Bible");

print("\n5. Checking in book ...");
library.check_in("The Bible");
print(library);

print("\n6. Removing book from library ...");
library.remove_book("Game of Thrones");
library.remove_book("Eragon");
print(library);
#END
