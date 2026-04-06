import unittest


def find_unsorted(arr):
    n = len(arr)
    if n <= 1:
        return (-1, -1)

    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    if left == n - 1:
        return (-1, -1)

    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1

    sub = arr[left: right + 1]
    sub_min = min(sub)
    sub_max = max(sub)

    while left > 0 and arr[left - 1] > sub_min:
        left -= 1

    while right < n - 1 and arr[right + 1] < sub_max:
        right += 1

    return (left, right)

"""                         TEST BLOCK                      """

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