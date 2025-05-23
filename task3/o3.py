import classes 
# PROGRAM START
menu = classes.Menu("Bank Account Management System");
bank = classes.Bank();

menu.add_option(bank.add_account, None, "Open a new account");
menu.add_option(bank.deposit, "F", "Deposit money into your account");
menu.add_option(bank.withdraw, "F", "Withdraw money from your account");
menu.add_option(bank.add_interest, "F", "Add interest to your account");
menu.add_option(bank.get_balance, None, "Get the current balance of your account");

menu.get_input();
# END
