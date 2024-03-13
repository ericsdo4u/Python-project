import unittest

from package_account.mybank import MyBank


class MyTestCase(unittest.TestCase):
    def test_register_customer(self):
        ddon_bank = MyBank("DonalhdBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        self.assertEqual(1, ddon_bank.number_of_customer())

    def test_register_two_customers(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.register_customer("donald", "eric", "1234")
        self.assertEqual(2, ddon_bank.number_of_customer())

    def test_check_balance(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        self.assertEqual(0, ddon_bank.check_balance(1, "1234"))

    def test_deposit_money_in_my_account(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.deposit_in_bank(120, 1)
        self.assertEqual(120, ddon_bank.check_balance(1, "1234"))

    def test_deposit_money_two_times_in_my_account(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.deposit_in_bank(120, 1)
        ddon_bank.deposit_in_bank(120, 1)
        self.assertEqual(240, ddon_bank.check_balance(1, "1234"))

    def test_withdraw_money_in_my_account(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.deposit_in_bank(200, 1)
        ddon_bank.withdraw_in_bank(120, 1, "1234")
        self.assertEqual(80, ddon_bank.check_balance(1, "1234"))

    def test_deposit_money_two_times_in_my_account_and_withdraw_once(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.deposit_in_bank(200, 1)
        ddon_bank.deposit_in_bank(200, 1)
        ddon_bank.withdraw_in_bank(100, 1, "1234")
        self.assertEqual(300, ddon_bank.check_balance(1, "1234"))

    def test_bank_transfer_system(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.deposit_in_bank(100, 1)
        ddon_bank.deposit_in_bank(100, 1)
        ddon_bank.transfer(100, 1, 2, "1234")
        self.assertEqual(100, ddon_bank.check_balance(1, "1234"))

    def test_remove_account_from_mybank(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.remove_account(1, "1234")
        self.assertEqual(1, ddon_bank.number_of_customer())

    def test_register_two(self):
        ddon_bank = MyBank("DonalhdBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.register_customer("donalt", "erit", "1235")
        ddon_bank.register_customer("donalm", "erim", "1236")
        self.assertEqual(3, ddon_bank.number_of_customer())

    def test_find_account(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        self.assertEqual(1, ddon_bank.number_of_customer())

    def test_add_and_find_account(self):
        ddon_bank = MyBank("DonaldBank")
        ddon_bank.register_customer("donald", "eric", "1234")
        ddon_bank.register_customer("donald", "eric", "1234")
        sample_input = ddon_bank.find_account(2)
        self.assertEqual(sample_input, ddon_bank.customers_list[1])


if __name__ == '__main__':
    unittest.main()
