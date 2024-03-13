import sys
from package_account.exception_class import *

from package_account.mybank import MyBank


class Main_APP:
    mybank = MyBank("ddonBank")

    def main(self):
        while True:
            print("""Welcome to ddon_bank, how may we be of help, select option :
                (1) Account registration
                (2) Deposit money
                (3) Check balance
                (4) Withdraw money
                (5) Transfer money
                (6) Remove account
                (7) Find account
                (8) Return back to the main manu
                (9) Exit app

                    """)
            try:
                option = int(input("Pick from the list of item from (1 - 7) for a quality service :"))
                match option:
                    case 1:
                        self.account_reg()
                        break
                    case 2:
                        self.deposit_money()
                        break
                    case 3:
                        self.check_balance()
                        break
                    case 4:
                        self.withdraw_money()
                        break
                    case 5:
                        self.transfer_money()
                        break
                    case 6:
                        self.remove_account()
                        break
                    case 7:
                        self.find_account()
                        break
                    case 8:
                        self.main()
                    case 9:
                        sys.exit()
            except ValueError:
                print("input missmatch, please select the right option")

    def account_reg(self):
        try:
            first_name = input("Enter first name : ")
            last_name = input("Last name : ")
            pin = int(input("choose a pin : "))
            if first_name and last_name and pin:
                self.mybank.register_customer(first_name, last_name, pin)
                print("customer successfully registered")
        except ValueError:
            print("Only digit is allow")

        self.main()

    def deposit_money(self):
        try:
            amount = int(input("Enter amount : "))
            account_number = int(input("Enter account number : "))
            if self.mybank.find_account(account_number) and amount > 0:
                self.mybank.deposit_in_bank(amount, account_number)
                print("Deposit successful")
            else:
                print("Invalid amount")
        except ValueError:
            print("Invalid entry")

        self.main()

    def check_balance(self):
        try:
            account_number = int(input("Enter account number : "))
            pin = int(input(" Enter pin number : "))
            if self.mybank.find_account(account_number):
                balance = self.mybank.check_balance(account_number, pin)
                print("Balance is ", balance)
            else:
                print("Account not found")
        except InvalidPinException:
            print("Invalid entry")

        self.main()

    def withdraw_money(self):
        try:
            amount = int(input("Enter amount : "))
            account_number = int(input("Enter account number : "))
            pin = int(input("Enter pin number : "))
            if self.mybank.find_account(account_number):
                self.mybank.withdraw_in_bank(amount, account_number, pin)
                print("withdraw successful")
            else:
                print("Account not found")
        except ValueError:
            print("Invalid amount")

        self.main()

    def transfer_money(self):
        try:
            amount = int(input("Enter amount : "))
            sender_account_number = int(input("Enter sender account number : "))
            receiver_account_number = int(input("Receiver account number : "))
            pin = int(input("Enter Pin number : "))
            if self.mybank.find_account(sender_account_number) and self.mybank.find_account(receiver_account_number):
                if sender_account_number != sender_account_number and receiver_account_number != receiver_account_number:
                    self.mybank.transfer(amount, sender_account_number, receiver_account_number, pin)
                    print("Transfer successful")
                else:
                    print("Account can't transfer to itself")
        except ValueError:
            print("Invalid entry")

        self.main()

    def remove_account(self):
        try:
            account_number = int(input("Enter account number : "))
            pin = int(input("Enter pin number : "))
            if self.mybank.find_account(account_number):
                self.mybank.remove_account(account_number, pin)
                print("Successfully remove account")
        except ValueError:
            print("Invalid entry")

        self.main()

    def find_account(self):
        try:
            account_number = int(input("Enter account number : "))
            if self.mybank.find_account(account_number):
                self.mybank.find_account(account_number)
                print("Account found")
        except BaseException:
            print("Invalid entry")

        self.main()


main = Main_APP()
main.main()
