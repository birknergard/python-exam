# PROGRAM START
import classes 

menu = classes.Menu("Bank Account Management System");
bank = classes.BankAccount();

menu.add_option(bank.get_balance, None, "View current balance");
menu.add_option(bank.deposit, "F", "Deposit to bank");
menu.add_option(bank.withdraw, "F", "Withdraw from bank");
menu.add_option(bank.add_interest, "F", "Add interest to bank");

menu.get_input();
# END
