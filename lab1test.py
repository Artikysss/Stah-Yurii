import unittest
from lab1 import find_unsorted

class TestBlock(unittest.TestCase):

    def test_sorted_ascending(self):
        self.assertEqual(find_unsorted([1, 5, 14, 26, 522]), (-1, -1))

    def test_sorted_descending(self):
        self.assertEqual(find_unsorted([9, 6, 4, 3, 1]), (0, 4))

    def test_two_elements(self):
        self.assertEqual(find_unsorted([11, 3]), (0, 1))

    def test_no_peaks(self):
        self.assertEqual(find_unsorted([7, 3, 1, 2, 6]), (0, 4))

    def test_three_peaks(self):

        self.assertEqual(find_unsorted([1, 10, 2, 14, 3, 22, 4]), (1, 6))


if __name__ == '__main__':
    unittest.main()