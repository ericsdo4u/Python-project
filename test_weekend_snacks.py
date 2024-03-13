import unittest

import class_work
import weekend_snacks


class MyTestCase(unittest.TestCase):
    def test_that_my_set_can_function(self):
        actual = {2, 3, 5, 2, 3, 2, 6, 3, 4, 3}
        expected = {2, 3, 4, 5, 6}
        self.assertEqual(expected, weekend_snacks.add_numbers_to_set(actual))

    def test_that_my_string_can_swap(self):
        string_one = "abc"
        string_two = "xyz"
        result_string = "xyc abz"
        self.assertEqual(result_string, weekend_snacks.swap_string(string_one, string_two))

    def test_return_sum_of_set(self):
        actual = {2, 3, 4, 3, 3, 3, 3, 2, 6, 5, 7}
        expected = 27
        self.assertEqual(expected, weekend_snacks.sum_collection(actual))

    def test_remove_number(self):
        actual = {2, 3, 5, 2, 3, 2, 6, 3, 4, 3}
        expected = {2, 4, 5, 6}
        self.assertEqual(expected, weekend_snacks.remove_number(actual))


