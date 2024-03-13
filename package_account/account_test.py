import unittest

from package_account.account import Account
from package_account.exception_class import InsufficientFundException


class MyTestCase(unittest.TestCase):
    def test_check_account_balance_is_zero(self):
        ddon_account = Account("donaldBank", 0, "1234")
        self.assertEqual(0, ddon_account.get_balance("1234"))

    def test_check_account_deposit(self):
        ddon_account = Account("donaldBank", 0, "1234")
        ddon_account.deposit(200)
        self.assertEqual(200, ddon_account.get_balance("1234"))

    def test_check_account_deposit_Twice(self):
        ddon_account = Account("donaldBank", 0, "1234")
        ddon_account.deposit(200)
        ddon_account.deposit(300)
        self.assertEqual(500, ddon_account.get_balance("1234"))

    def test_check_account_withdraw(self):
        ddon_account = Account("donaldBank", 0, "1234")
        ddon_account.deposit(500)
        ddon_account.withdraw(300, "1234")
        self.assertEqual(200, ddon_account.get_balance("1234"))

    def test_check_account_withdraw_after_depositing_twice(self):
        ddon_account = Account("donaldBank", 0, "1234")
        ddon_account.deposit(500)
        ddon_account.deposit(500)
        ddon_account.withdraw(300, "1234")
        self.assertEqual(700, ddon_account.get_balance("1234"))

    def test_check_non_negative_balance(self):
        ddon_account = Account("donaldBank", 0, "1234")
        ddon_account.deposit(1000)
        ddon_account.withdraw(500, "1234")
        self.assertEqual(500, ddon_account.get_balance("1234"))
        self.assertRaises(InsufficientFundException, lambda: ddon_account.deposit(-1000))
