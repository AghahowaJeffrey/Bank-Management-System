"""" The main program file containing the main program loop and related functions."""""

from bank import Bank  # Import the Bank class from the bank module.
import pyinputplus as pyip  # Import pyinputplus for better input operations.


bank = Bank('Guaranteed Trust Bank', 'Nigeria - Benin City')  # Initializing a banking organization.


def account_login():
    """ A function that calls the login method from the bank instance
        when the user decides to log into an account.
    """
    print('Log into your desired account.\n')
    bank.login_validation(input('Number: '), input('Password: '))  # A call to the login method in the bank instance.


def buy_airtime():
    """ A function that calls the airtime_self method from the current logged in account instance
        stored in the bank instance when the user decides to buy airtime.

        amount - The amount(int) of airtime.
    """
    amount = int(input("Amount:\n"))
    # Checks for the present of a created account in the bank but not yet logged in, to become the current account.
    if (bank.current_account is None) and len(bank.accounts) > 0:  # Prompts user to login in.
        print('Kindly log into your account to perform transactions.\n\n')
    # No account has been created in the bank.
    elif bank.current_account is None and len(bank.accounts) == 0:  # Informs user that there's no created account.
        print('You have no account with this bank.\n')
    else:
        # A call to the airtime_self method of current account if there is an account that is logged in.
        bank.current_account.airtime_self(amount)


def airtime_others():
    """ A function that calls the airtime_others method from the current logged in account instance
        stored in the bank instance, when the user decides to buy airtime.

        recipient_number - The number(str) of the recipient.
        amount - The amount(int) of airtime.
    """
    recipient_number = input("Recipient's number:\n")
    amount = int(input("Amount:\n"))
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        # A call to the airtime_others method of current account if there is an account that is logged in.
        bank.current_account.airtime_others(amount, recipient_number)


def data():
    """ A function that calls the buy_data method from the current logged in account instance
        stored in the bank instance, when the user decides to buy data.

        response - Option selected by the user(self/other).
        amount - the amount(int) of data.
    """
    response = pyip.inputMenu(['Self', 'Others'], numbered=True)
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        if response == 'Self':
            amount = int(input('Amount:\n'))
            # A call to the buy_data method of the currently logged in account if response is self.
            bank.current_account.buy_data(amount)
        elif response == 'Others':
            recipient_number = input("Recipient's number:\n")
            amount = int(input("Amount:\n"))
            # A call to the buy_data method of currently logged in account if response is others.
            bank.current_account.buy_data(amount, recipient_number)


def transfer_bank():
    """ A function that calls the transfer_bank method from the current logged in account instance
        stored in the bank instance, when the user decides to transfer money to same bank.

        acct_num - The account number(str) of the recipient.
        amount - The amount(int) 0f money.
    """
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        acct_num = input('Account number:\n')
        amount = int(input('Amount:\n'))
        # A call to the transfer_bank method of current account if there is an account that is logged in.
        bank.current_account.transfer_bank(acct_num, amount)


def transfer_other():
    """ A function that calls the transfer_other_bank method from the current logged in account instance
        stored in the bank instance, when the user decides to transfer money to a different bank.

        bank name = The name of the recipient bank(str).
        acct_num - The account number(str) of the recipient.
        amount - The amount(int) 0f money.
       """
    bank_name = input('Bank:\n')
    acct_num = input('Account number:\n')
    amount = int(input('Amount:\n'))
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        # A call to the transfer_other_bank method of current account if there is an account that is logged in.
        bank.current_account.transfer_other_bank(acct_num, amount, bank_name)


def deposit():
    """ A function that calls the deposit method from the current logged in account instance
        stored in the bank instance, when the user decides to deposit money into his account.

        amount - The amount(int) 0f money.
    """
    amount = int(input('Amount:\n'))
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        # A call to the deposit method of current account if there is an account that is logged in.
        bank.current_account.deposit(amount)


def account_balance():
    """ A function that calls the balance method from the current logged in account instance
        stored in the bank instance, when the user decides to check his account balance.
    """
    if (bank.current_account is None) and len(bank.accounts) > 0:
        print('Kindly log into your account to perform transactions.\n\n')
    elif bank.current_account is None:
        print('You have no account with this bank.\n')
    else:
        # A call to the account_balance method of current account if there is an account that is logged in.
        bank.current_account.account_balance()


def open_account():
    """ A function that calls the open_account method from the bank instance,
        when the user decides to open an account.

        name - Name of the individual(str).
        age - Age of the individual(str).
        phone_num - Phone number of the individual(str).
        pin - Security pin for confirming transactions(str).
    """
    import re  # Imports re for regex operation.
    name = input('Full name:\n')
    age = input('Age:\n')
    phone_num = input('Phone Number:\n')
    pin = input('Pin:\n')
    # Continuously prompts the user to repeat pin until the repeated pin is same as the previous pin.
    pyip.inputStr(prompt='Input pin again:\n', allowRegexes=[re.compile(rf'{pin}')],
                  blockRegexes=[re.compile(r'.*')])
    # A call to the open_account method of the bank instance.
    bank.open_account(name, age, phone_num, pin)


def main():  # The main program function.
    """The user interface - Various options for user to select from.
    """
    decision = pyip.inputMenu(choices=['Account-Login', 'Airtime-Self', 'Airtime-Other', 'Data',
                                       f'Trsf-{bank.bank_name}', 'Trsf-Others', 'Open Account',
                                       'Deposit', 'A/C Balance', 'Exit'], numbered=True)

    if decision == 'Account-Login':  # Calls account_login function if user decision is 1.
        account_login()

    if decision == 'Airtime-Self':  # Calls the buy_airtime function if user decision is 2.
        buy_airtime()

    if decision == 'Airtime-Other':  # Calls the airtime_others function if user decision is 3.
        airtime_others()

    if decision == 'Data':  # Calls the data function if user decision is 4.
        data()

    if decision == f'Trsf-{bank.bank_name}':  # Calls the transfer_bank function if user decision is 5.
        transfer_bank()

    if decision == 'Trsf-Others':  # Calls the transfer_other function if user decision is 6.
        transfer_other()

    if decision == 'Open Account':  # Calls the open_account function if user decision is 7.
        open_account()

    if decision == 'Deposit':  # Calls the deposit function if user decision is 8.
        deposit()

    if decision == 'A/C Balance':  # Calls the account_balance function if user decision is 9.
        account_balance()

    if decision == 'Exit':  # Exits the program if  user decision is 10.
        exit()


if __name__ == '__main__':  # Will run this code if the program is run from this file.
    while True:  # The main program loop.
        main()


