import unittest
import dispatchers_payment_app


class MyTestCase(unittest.TestCase):
    def test_that_the_rateing_is_80_and_expected_result_is_45000(self):
        self.assertEqual(45000, dispatchers_payment_app.dispatchers_payment_system(80))

    def test_that_the_rateing_is_25_and_expected_result_is_9000(self):
        self.assertEqual(9000, dispatchers_payment_app.dispatchers_payment_system(25))

    def test_that_the_rateing_is_not_negative(self):
        self.assertRaises(ValueError, lambda: dispatchers_payment_app.dispatchers_payment_system(-80))  # add assertion here


if __name__ == '__main__':
    unittest.main()
