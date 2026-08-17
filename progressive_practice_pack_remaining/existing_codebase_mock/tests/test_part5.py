import unittest
import numpy as np

from sampling import sample_rows


class Part5Test(unittest.TestCase):

    def test_deterministic(self):
        probs = np.array([
            [0.1, 0.2, 0.7],
            [0.4, 0.6, 0.0],
        ])

        a = sample_rows(probs, seed=123)
        b = sample_rows(probs, seed=123)

        self.assertEqual(a, b)

    def test_rows_are_normalized(self):
        probs = np.array([
            [1.0, 1.0],
            [1.0, 3.0],
        ])

        result = sample_rows(probs, seed=5)

        self.assertEqual(len(result.indices), 2)
        self.assertTrue(all(i in (0, 1) for i in result.indices))

    def test_nan_row_invalid(self):
        probs = np.array([
            [0.5, np.nan, 0.5],
        ])

        with self.assertRaises(ValueError):
            sample_rows(probs, seed=1)

    def test_zero_sum_row_invalid(self):
        probs = np.array([
            [0.0, 0.0, 0.0],
        ])

        with self.assertRaises(ValueError):
            sample_rows(probs, seed=1)

    def test_result_type_preserved(self):
        probs = np.array([[0.5, 0.5]])
        result = sample_rows(probs, seed=1)
        self.assertIsInstance(result.indices, tuple)


if __name__ == "__main__":
    unittest.main()
