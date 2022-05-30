"""" This file contains the account class and all it's related attributes and methods. """""

from bank import Bank  # Imports the Bank class from the bank module.


class Account(Bank):
    def __init__(self, account_num, name, number, age, pin, bank_name, bank_location):
        super().__init__(bank_name, bank_location)
        self.account_num = account_num
        self.name = name
        self.number = number
        self.age = age
        self.pin = pin
        self.balance = 0
        self.bank_charge = 5

    def airtime_self(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f'Your recharge of {amount} naira was successful.\n')
        else:
            print('Insufficient balance.\n')

    def airtime_others(self, amount, recipient_number):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f'You have successfully recharged {recipient_number} with {amount} naira.\n')
        else:
            print('Insufficient balance.\n')

    def buy_data(self, amount, recipient_number=None):
        if self.balance - amount >= 0:
            self.balance -= amount
            if recipient_number is None:
                print(f'You have successfully recharged with {amount} naira data.\n')
            elif recipient_number is not None:
                print(f'You have successfully recharged {recipient_number} with {amount} naira data.\n')
        else:
            print('Insufficient balance.\n')

    def transfer_bank(self, account, amount):
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
        pin = input('Pin:\n')
        if pin == self.pin:
            self.balance += amount
            print(f'You have successfully deposited {amount} naira into your account.\n')
        else:
            print('Invalid pin.')

    def account_balance(self):
        self.balance -= self.bank_charge
        print('------Account Balance------\n'
              f'Your balance is {self.balance} naira(#)'
              f'\n\n')

    def __str__(self):
        return f'Account({self.account_num}, {self.name}, {self.number}, ' \
               f'{self.age}, {self.pin}, {self.bank_name}, {self.bank_location})'

