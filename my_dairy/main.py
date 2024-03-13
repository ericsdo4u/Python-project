from package_account.mybank import MyBank


class Display_account:
    def __init__(self):
        self.ddon_bank = MyBank("DonaldBank")

    def main(self):
        MyBank("DonaldBank")
        print("""Welcome to ddon_bank, how may we be of help, select option : 
            (1) Account registration
            (2) Deposit money
            (3) Check balance
            (4) Withdraw money
            (5) Transfer money
            (6) Remove account
            (7) Exit app

            """)

        option = input("Pick from the list of item from (1 - 7) for a quality service :")

        match option:
            case 1:
                self.account_reg()

        # case 2:

    def account_reg(self):
        first_name = input("Enter first name :")
        last_name = input("Last name :")
        pin = input("choose a pin")
        self.ddon_bank.register_customer(first_name, last_name, pin)
        print("customer successfully registered")





