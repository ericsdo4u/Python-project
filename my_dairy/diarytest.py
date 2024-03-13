import unittest

from dairy import *


class MyTestCase(unittest.TestCase):
    def test_create_one_dairy_entry(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.create_entry("foodie", "food items")
        self.assertEqual(1, ddon_dairy.get_number_of_entry())

    def test_find_account_by_id(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.create_entry("foodie", "food items")
        self.assertEqual(1, ddon_dairy.get_number_of_entry())

    def test_find_account_by_id_two_entry(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.create_entry("foodie", "food items")
        ddon_dairy.create_entry("foodie", "food items")
        sampe_input = ddon_dairy.find_entry_by_id(2)
        print(sampe_input.get_entry_id())
        self.assertEqual(2, ddon_dairy.get_number_of_entry())

    def test_dairy_delete_entry(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.create_entry("foodie", "food items")
        # ddon_dairy.create_entry("foodie", "food items")
        ddon_dairy.create_entry("foodie", "food items")
        ddon_dairy.delete_entry(2)
        self.assertEqual(1, ddon_dairy.get_number_of_entry())

    def test_update_entry(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.create_entry("foodie", "food items")
        entry = ddon_dairy.find_entry_by_id(1)
        ddon_dairy.update_entry(1, "My_foodie", "my_food item")
        print(entry.get_body())
        self.assertEqual("my_food item", entry.get_body())

    def test_locked_my_dairy(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.lock_dairy()
        self.assertTrue(ddon_dairy.is_locked())

    def test_locked_my_dairy_no_new_entry_until_is_unlocked(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.lock_dairy()
        self.assertTrue(ddon_dairy.is_locked())
        self.assertRaises(ValueError, lambda: ddon_dairy.create_entry("foodie", "food items"))

    def test_unlock_my_dairy(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.lock_dairy()
        self.assertTrue(ddon_dairy.is_locked())
        ddon_dairy.unlock_dairy("1234")
        self.assertFalse(ddon_dairy.is_locked())

    def test_unlock_my_dairy_and_add_entry(self):
        ddon_dairy = Diary("ddon", "1234")
        ddon_dairy.lock_dairy()
        self.assertTrue(ddon_dairy.is_locked())
        ddon_dairy.unlock_dairy("1234")
        self.assertFalse(ddon_dairy.is_locked())
        ddon_dairy.create_entry("foodie", "food items")
        self.assertEqual(1, ddon_dairy.get_number_of_entry())


if __name__ == '__main__':
    unittest.main()
