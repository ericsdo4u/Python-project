import unittest

from test.segment_display import Seven_Segment


class MyTestCase(unittest.TestCase):
    def test_sample_size(self):
        show_me = Seven_Segment()
        self.assertEqual([], show_me.get_size())

    def test_That_only_digit_input_allow(self):
        show_me = Seven_Segment()
        sample_input = []
        self.assertEqual([], show_me.get_size())


if __name__ == '__main__':
    unittest.main()
