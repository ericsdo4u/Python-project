from package_account.account import Account
from package_account.exception_class import InsufficientFundException


class Dairy:
    def __init__(self, name):
        self.account_number = 0
        self.name = name
        self.customers_list = []

    def get_name(self):
        return self.name

    def get_account_number(self):
        self.account_number += 1
        return self.account_number

    def find_account(self, account_number) -> Account:
        try:
            for account in self.customers_list:
                if account.get_account_number1() == account_number:
                    return account
                else:
                    print("Account not found")
        except BaseException:
            print("Invalid entry")
        # raise InvalidAccountNumberException("Account not found")

    def check_balance(self, account_number, pin) -> int:
        try:
            account_found = self.find_account(account_number)
            return account_found.get_balance(pin)
        except InsufficientFundException:
            print("Insufficient fund")

    def number_of_customer(self) -> int:
        return len(self.customers_list)

    def register_customer(self, first_name, last_name, pin) -> Account:
        name = first_name + " " + last_name
        new_account = Account(name, self.get_account_number(), pin)
        self.customers_list.append(new_account)
        print("your account number is : ", new_account.get_account_number1())
        return new_account

    def deposit_in_bank(self, amount, account_number):
        try:
            account_found = self.find_account(account_number)
            account_found.deposit(amount)
        except BaseException:
            print("No Negative value")

    def withdraw_in_bank(self, amount, account_number, pin):
        amount_withdraw = self.find_account(account_number)
        amount_withdraw.withdraw(amount, pin)
        # for account in self.customers_list:
        #     if account.get_account_number1() == account_number:
        #         if account.pin == pin:
        #             withdraw_amount = account.withdraw(amount, pin)
        #             return withdraw_amount

    def transfer(self, amount, sender_account_number, receiver_account_number, pin):
        try:
            sender = self.find_account(sender_account_number)
            receiver = self.find_account(receiver_account_number)
            sender.withdraw(amount, pin)
            receiver.deposit(amount)
        except ValueError:
            print("Invalid entry")

    def remove_account(self, account_number, pin):
        try:
            for account in self.customers_list:
                if account.get_account_number1() == account_number and account.pin == pin:
                    self.customers_list.remove(account)
        except ValueError:
            print("Account not found")
