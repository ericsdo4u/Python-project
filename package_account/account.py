from package_account.exception_class import *
from package_account.exception_class import InsufficientFundException


class Account:

    def __init__(self, name, account_number, pin):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.account_number = account_number

    def name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def get_account_number1(self):
        return self.account_number

    def get_balance(self, pin) -> int:
        if self.pin == pin:
            return self.balance
        raise InsufficientFundException("Insufficient balance")

    def deposit(self, amount):
        try:
            if amount > 0:
                self.balance += amount
            else:
                raise InsufficientFundException("We don't accept negative value")
        except ValueError:
            print("Invalid amount")

    def withdraw(self, amount, pin):
        try:
            if self.pin == pin:
                if 0 < amount <= self.balance:
                    self.balance -= amount
                else:
                    raise ValueError("Negative amount not allowed")
        except InsufficientFundException:
            print("Insufficient fund")

    @property
    def validate_pin(self):
        return self.pin

    @validate_pin.setter
    def validate_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinException("Pin not correct")
        else:
            self.pin = pin
