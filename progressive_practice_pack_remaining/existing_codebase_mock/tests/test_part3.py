import unittest
import numpy as np

from normalize import masked_normalize


class Part3Test(unittest.TestCase):

    def test_basic_normalization(self):
        values = np.array([
            [1.0, 1.0, 2.0],
            [2.0, 3.0, 5.0],
        ])
        mask = np.array([
            [True, True, True],
            [True, True, True],
        ])

        result = masked_normalize(values, mask)

        np.testing.assert_allclose(
            result,
            np.array([
                [0.25, 0.25, 0.5],
                [0.2, 0.3, 0.5],
            ]),
            equal_nan=True,
        )

    def test_masked_positions_are_nan(self):
        values = np.array([[1.0, 2.0, 3.0]])
        mask = np.array([[True, False, True]])

        result = masked_normalize(values, mask)

        np.testing.assert_allclose(
            result,
            np.array([[0.25, np.nan, 0.75]]),
            equal_nan=True,
        )

    def test_nan_values_are_ignored_in_sum(self):
        values = np.array([[1.0, np.nan, 3.0]])
        mask = np.array([[True, True, True]])

        result = masked_normalize(values, mask)

        np.testing.assert_allclose(
            result,
            np.array([[0.25, np.nan, 0.75]]),
            equal_nan=True,
        )

    def test_zero_sum_row_becomes_nan(self):
        values = np.array([[0.0, 0.0, 3.0]])
        mask = np.array([[True, True, False]])

        result = masked_normalize(values, mask)

        self.assertTrue(np.isnan(result[0, 0]))
        self.assertTrue(np.isnan(result[0, 1]))
        self.assertTrue(np.isnan(result[0, 2]))


if __name__ == "__main__":
    unittest.main()
