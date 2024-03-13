import unittest
import reverse_Order

class MyTestCase(unittest.TestCase):

    def test_That_the_value_Of_Reverse_Order_Can_Be_Sorted(self):
        first_List = [8, 7, 10, 4, 2, 13, 6, 9]
        second_List = [2, 4, 6, 7, 8, 9, 10, 13]
        self.assertEqual(second_List, reverse_Order.reverse_Order_Number(first_List))

    def test_For_Descending_Order(self):
        first_List = [8, 7, 10, 4, 2, 13, 6, 9]
        second_List = [13, 10, 9, 8, 7, 6, 4, 2]
        self.assertEqual(second_List, reverse_Order.maintain_Order_Number(first_List))

