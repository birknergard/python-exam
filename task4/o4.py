def is_palindrome():
    new_string = input("Enter a string, and i will check if its a palindrome.\n --> ");
    if len(new_string) <= 1:
        print("String is too short. Needs to be at least 2 characters.");
        return;

    if not new_string.isalpha():
        print("String needs to consist of letters a-z or A-Z");
        return;

    y = len(new_string) - 1;
    for i in range(0, int(len(new_string) / 2)):
        if new_string[i] != new_string[y]:
            print("This string is not a palindrome.");
            return;
        y -= 1;
        
    print("Given string is a palindrome!");
#ndef | Running program ... 
is_palindrome();
