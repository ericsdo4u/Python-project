import unittest


import twomethods


class TestTwoMethods(unittest.TestCase):
    def test_get_string(self):
        sample_word = TwoMethods.TwoMethod()
        sample_word.getString("hello word")
        self.assertEqual("HELLO WORD", sample_word.printString())
