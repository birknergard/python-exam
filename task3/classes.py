import os
import math

class Option:
    def __init__(self, func, arg_type, title):
        self._title = title;
        self.__func = func;

        # Args is a string of either (N)umber or (S)tring,
        # Is used to determine which datatype the function requires
        if type(arg_type) is str: 
            self.__type = arg_type.upper();
        else:
            self.__type = None;


    def run(self):

        if self.__type == "S":
            parsed_arg = input("Enter a string.\n--> ");
            self.__func(parsed_arg);

        elif self.__type == "N":
            arg = input("Enter a whole number.\n--> ");

            parsed_arg = int(arg);
            self.__func(parsed_arg);


        elif self.__type == "F":
            arg = input("Enter a number.\n--> ");

            parsed_arg = float(arg);

            self.__func(parsed_arg);

        # Runs the function without argument if arg is anything else
        else:
            self.__func();



class Menu:
    def __init__(self, name):
        self.__program_name = name;
        self.__options = [];

    def __option_count(self):
        return len(self.__options);

    def add_option(self, method, arg_type, title):
        self.__options.append(Option(method, arg_type, title));

    def get_input(self):
        while(True):

            # Clears the terminal
            os.system("clear");

            print(f"\n{self.__program_name}");
            print(50 * "=");

            for i, option in enumerate(self.__options):
                print(f"{i + 1}) {option._title}");

            print(f"\n0) Exit");

            print(50 * "=");
            print("");

            # Take and validate input
            selection = input("Please enter your selection by number\n--> "); 
            if not selection.isdigit():
                print("Selection has to be a valid digit.");
                continue;

            selection = int(selection);
            if selection > self.__option_count():
                print("Invalid option.");
                continue;

            # Exit option is 0
            if selection == 0:
                print("Exiting ...");
                return;

            # Otherwise, run option
            self.__options[selection - 1].run();

            input("\n>Press enter to continue<");


class BankAccount:
    def __init__(self):
        self.balance = 0;

    def get_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount;
            print(f"Added {amount} to balance.");
        else:
            print("Can't add negative value.");

    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount;
            print(f"Withdrew {amount} from balance");
        else:
            print("Cannot withdraw given amount from balance.");


    def add_interest(self, rate):
        # Ensures interest is a double between 0 and 1. 
        # Input is required to be a decimal number between 0 and 100; 
        if rate <= 0 or rate > 100:
            print("Invalid interest. Has to be number between 0 and 100");
        else:
            # Converts from percentage to decimal and adds the interest
            interest = math.floor(self.balance * (rate / 100));
            self.balance += interest;
            print(f"Added {rate}% worth of interest ({interest},-) to balance.");

