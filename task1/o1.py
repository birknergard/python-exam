# PYTHON EXAM
# TASK 1
import random as rand
import os

try:
    word_file = open("words.txt", "r");
    # Reads a line from the file, removes \n and whitespace, and splits it on " "
    word_list = word_file.readline().strip().split(",");
    rand_int = rand.randint(0, len(word_list) - 1) ;

    word_rand = word_list[rand_int];

    word_empty = [];

    # List of guessed letters
    word_set = set(); 

    # Dictionary: "letter" : indexes in word [index1, index2, ...]
    word_dict = dict();

    print("Checking words ...");
    # Figure out how many words

    # Load letters into dictionary for simpler lookup
    previous_index = 0;
    for i in range(0, len(word_rand)):
        char = word_rand[i];

        # First entry, create the array
        if char not in word_dict:
            word_dict[char] = [];

        # App letter to dictionary 
        word_dict[char].append(i);
        word_empty.append("_");


    # Program start
    print("Welcome to the word guessing game!");
    print("A random word will be chosen and you will have to guess it through guessing letters.");
    print(f"\nYour word has {len(word_rand)} letters. Good luck!\n\n");

    input("> Press ENTER to continue <\n");
    os.system("clear");

    guesses = 8;
    while guesses > 0:

        # if its empty, break the loop and congratulate the user etc etc.
        if len(word_dict) == 0:
            print(f"\n\nYou guessed all the letters!\nThe word was -> \"{word_rand}\"");
            break;

        # print the letters found, or empty spots, of the word
        print(f"\nYou have {guesses} guesses left.");
        for letter in word_empty:
            print(f"{letter} ", end = "");
        print("\n");

        # Take user input
        guess = input("Guess a character: ");

        # Ensure input is valid
        # Should only be one character.
        if len(guess) > 1:
            os.system("clear");
            print("You may only guess one character at a time.", end = "");
            guesses -= 1;
            continue;

        if guess.isalpha() != True:
            os.system("clear");
            print("You have to guess a letter.", end = "");
            continue;
            

        #If user attempts to guess an already found word,
        # Remove a guess and tell the user its already been found.
        if guess in word_set: 
            print("That letter has already been guessed", end = "");
            guesses -= 1;
            os.system("clear");
            continue;

        # Lookup in the dictionary for the letter.
        if guess in word_dict:
            #If letter is found, add the letter to the empty word on the containing indices, 
            # and remove the letter from the dictionary. Add to another dictionary(?) containing
            # Words that have been found.
            for index in word_dict[guess]:
                word_empty[index] = guess;
            word_dict.pop(guess);
            word_set.add(guess);
            os.system("clear");


        #If the guess is just wrong: Tell them its wrong, 
        # then subtract a guess.
        else:
            os.system("clear");
            print("Sorry, that letter is not in the word.", end = "");
            guesses -= 1;
        

    if guesses == 0:
        print(f"\n\nYou ran out of guesses!\nThe word was -> \"{word_rand}\"");
    print("\nThank you for playing!\nYou may restart the program to play another round.");

    word_file.close();
except IOError:
    print("File not found.");
#END
