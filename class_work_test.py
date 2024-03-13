import unittest

import class_work
import wordcount


class MyTestCase(unittest.TestCase):
    def test_Add_Number_To_List(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(10, class_work.get_Length_Of_List(first))

    def test_Sum_Of_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(70, class_work.sum_All_Elemet_Of_Even(first))

    def test_Sum_Of_Element1(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(75, class_work.sum_Odd_Element(first))

    def test_multiply_Element_In_Third_Position(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(39, class_work.multiply_Element_In_Third_Position(first))

    def test_average_Element_in_list(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(7.632, class_work.average_Element_in_list(first))

    def test_largest_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(19, class_work.largest_Element(first))

    def test_smallest_Element(self):
        first = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.assertEqual(10, class_work.smallest_Element(first))

    def test_Word_Count_In_A_List_Of_Word(self):
        text = ('The palace is minuts away from he village'
                ' this is sample text with several words '
                'this is more sample text with some different words ')
        self.assertEqual(17, class_work.count_word(text))

    def test_sum_of_even_and_odd_number(self):
        sample_input = 10
        expected_output = 20, 25
        self.assertEqual(expected_output, class_work.sum_even_and_odd_numbers(sample_input))

    def test_function_can_count_word(self):
        word_input = "hello world, 123"
        expected = '("NUMBERS" 3 "LETTERS", 10)'
        self.assertEqual(expected, wordcount.count_word(word_input))

    def test_function_can_count_upper_and_lower_case(self):
        word_input = "HELlo worlD"
        expected = '("UPPER_LETTERS" 4 "LOWER_LETTERS" 6)'
        self.assertEqual(expected, wordcount.count_upper_lower(word_input))
