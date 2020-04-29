import unittest
from RemoveDuplicatesfromSortedArray import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.list = [0, 1, 1, 2, 2, 2, 3, 4]
        self.assertEqual(temp.removeDuplicates(self.list),5)
    def test_all_different(self):
        temp = Solution()
        self.list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(temp.removeDuplicates(self.list),8)

if __name__ == "__main__":
    unittest.main()
