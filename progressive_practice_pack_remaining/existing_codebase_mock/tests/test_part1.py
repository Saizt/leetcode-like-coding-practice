import unittest
import numpy as np

from stats import batch_stats


class Part1Test(unittest.TestCase):

    def test_regular_rows(self):
        arr = np.array([
            [1.0, 2.0, 3.0],
            [-1.0, 4.0, 2.0],
        ])

        result = batch_stats(arr)

        self.assertEqual(result[0].minimum, 1.0)
        self.assertEqual(result[0].maximum, 3.0)
        self.assertEqual(result[0].total, 6.0)

        self.assertEqual(result[1].minimum, -1.0)
        self.assertEqual(result[1].maximum, 4.0)
        self.assertEqual(result[1].total, 5.0)

    def test_nan_values_ignored(self):
        arr = np.array([
            [1.0, np.nan, 3.0],
        ])

        result = batch_stats(arr)[0]

        self.assertEqual(result.minimum, 1.0)
        self.assertEqual(result.maximum, 3.0)
        self.assertEqual(result.total, 4.0)

    def test_all_nan_row(self):
        arr = np.array([[np.nan, np.nan]])

        result = batch_stats(arr)[0]

        self.assertTrue(np.isnan(result.minimum))
        self.assertTrue(np.isnan(result.maximum))
        self.assertTrue(np.isnan(result.total))


if __name__ == "__main__":
    unittest.main()
