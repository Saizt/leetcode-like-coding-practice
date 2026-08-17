import unittest
import numpy as np

from buckets import bucketize


class Part2Test(unittest.TestCase):

    def test_bucketize(self):
        token_ids = np.array([0, 1, 2, 3, 4, 5])
        result = bucketize(token_ids, 3)
        np.testing.assert_array_equal(result, np.array([2, 2, 2]))

    def test_large_ids_use_modulo(self):
        token_ids = np.array([3, 4, 7, 8])
        result = bucketize(token_ids, 3)
        np.testing.assert_array_equal(result, np.array([1, 1, 2]))

    def test_empty_input(self):
        result = bucketize(np.array([], dtype=int), 4)
        np.testing.assert_array_equal(result, np.array([0, 0, 0, 0]))

    def test_negative_ids_invalid(self):
        with self.assertRaises(ValueError):
            bucketize(np.array([1, -1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
