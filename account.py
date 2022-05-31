"""" This file contains the account class and all it's related attributes and methods. """""

from bank import Bank  # Imports the Bank class from the bank module.


class Account(Bank):
    """ An account class that contains attributes and methods. """

    def __init__(self, account_num, name, number, age, pin, bank_name, bank_location):
        """ Initializing the fields of account objects"""
        super().__init__(bank_name, bank_location)  # Inherits the attributes of the bank class.
        self.account_num = account_num  # Account number.
        self.name = name  # Account owner's name.
        self.number = number  # Account owner's number.
        self.age = age  # Account owner's age.
        self.pin = pin  # Security transfer pin.
        self.balance = 0  # Account balance.
        self.bank_charge = 5  # Bank charge.

    def airtime_self(self, amount):
        """ A method that performs the function of buying airtime from the account.
        """
        if self.balance - amount >= 0:  # Checks to see if balance is greater or equal to amount.
            self.balance -= amount  # Deducts amount from balance.
            print(f'Your recharge of {amount} naira was successful.\n')
        else:
            print('Insufficient balance.\n')

    def airtime_others(self, amount, recipient_number):
        """ A method that performs the function of buying airtime for others."""
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f'You have successfully recharged {recipient_number} with {amount} naira.\n')
        else:
            print('Insufficient balance.\n')

    def buy_data(self, amount, recipient_number=None):
        """ A method that performs the function of buying data from the account."""
        if self.balance - amount >= 0:
            self.balance -= amount
            if recipient_number is None:
                print(f'You have successfully recharged with {amount} naira data.\n')
            elif recipient_number is not None:
                print(f'You have successfully recharged {recipient_number} with {amount} naira data.\n')
        else:
            print('Insufficient balance.\n')

    def transfer_bank(self, account, amount):
        """ A method that performs the function of transferring money to another account in the same bank. """
        if self.balance - amount >= 0:
            pin = input('Pin:\n')
            if pin == self.pin:
                self.balance -= amount + self.bank_charge
                print(f'You have successfully transferred {amount} naira to {account}.\n')
            else:
                print('Invalid pin.')
        else:
            print('Insufficient balance.\n')

    def transfer_other_bank(self, account, amount, bank_name):
        """ A method that performs the function of transferring money to another bank account."""
        if self.balance - amount >= 0:
            pin = input('Pin:\n')
            if pin == self.pin:
                self.balance -= amount + self.bank_charge
                print(f'You have successfully transferred {amount} naira to {bank_name}:{account}\n.')
            else:
                print('Invalid pin.')
        else:
            print('Insufficient balance.\n')

    def deposit(self, amount):
        """ A method that performs the function of adding money to the current balance of the account."""
        pin = input('Pin:\n')
        if pin == self.pin:  # checks if the supplied pin matches the pin of the account.
            self.balance += amount
            print(f'You have successfully deposited {amount} naira into your account.\n')
        else:
            print('Invalid pin.')

    def account_balance(self):
        """ A method that performs the function of displaying the current balance"""
        self.balance -= self.bank_charge # Deducts bank charges from the balance.
        print('------Account Balance------\n'
              f'Your balance is {self.balance} naira(#)'
              f'\n\n')  # Blank line

    def __str__(self):
        """ Human-readable representation of the object."""
        return f'Account({self.account_num}, {self.name}, {self.number}, ' \
               f'{self.age}, {self.pin}, {self.bank_name}, {self.bank_location})'

