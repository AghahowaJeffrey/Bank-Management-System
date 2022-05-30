"""" A model of a Bank Organization.
     This file contains the bank class and all it related attributes and methods.
 """""


class Bank:
    """ A bank class that contains attributes and methods. """

    accounts = []  # A list that stores all created account instance.

    def __init__(self, bank_name, bank_location):
        """ Initializes the fields of bank account objects."""
        self.bank_name = bank_name  # The name of the bank.
        self.bank_location = bank_location  # The geographical location of the bank.
        self.current_account = None

    def open_account(self, name, age, phone_num, pin):
        """ A method that creates a bank account for the particular bank
            By creating an instance of the account class and stores the instance in the bank. """
        from account import Account
        # Generates an account number for the person.
        import random  # Imports the random module.
        account_num = ''  # Stores the account number
        num = str(random.randint(0, 9))
        for i in range(2):
            account_num += num

        for x in range(8):
            num = random.randint(0, 9)
            account_num += str(num)

        # Stores the instance of the account in the accounts list in the bank.
        self.accounts.append(Account(account_num, name, phone_num, age, pin, self.bank_name, self.bank_location))
        self.current_account = None  # Log out of any previously logged in account.
        print('Your account has been successfully created:\n'
              f'Your account number is {account_num}\n')

    def login_validation(self, number, account_num):
        """ A method that loops through all the accounts stored in the bank class,
            And checks to see if the information provided matches any account previously stored."""
        state = False  # Login unsuccessful
        for account in range(len(self.accounts)):  # Loops through accounts.
            # Checks if number and account_num matches any account in accounts.
            if self.accounts[account].number == number and self.accounts[account].account_num == account_num:
                self.current_account = self.accounts[account]
                state = True  # Login successful
                print(f'Login successful\nWelcome {self.accounts[account].name}.\n\n')
                break

            # Runs this code if the login details are incorrect.
        if state is False:  # Checks if login is unsuccessful
            print('The logins do not match any account.\n'
                  'Confirm you have provided the right details.\n')
