from unittest import TestCase

import class_work


class Test(TestCase):
    def test_get_length_of_list(self):
        first = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

        self.assertEqual(10, Class_work.get_Length_Of_List(first))

#
# class Test(TestCase):
#     def sum_All_Elemet_Of_Even(self):
#         first = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#         self.assertEqual()
