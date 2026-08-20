import unittest
import numpy as np

from signal_garden.transforms import normalize, bucketize, row_score


class TransformTests(unittest.TestCase):
    def test_normalize_rows(self):
        x = np.array([
            [1.0, 2.0, 3.0],
            [10.0, 20.0, 30.0],
        ])

        actual = normalize(x)

        expected = np.array([
            [0.0, 0.5, 1.0],
            [0.0, 0.5, 1.0],
        ])

        np.testing.assert_allclose(actual, expected)

    def test_constant_row_normalizes_to_zero(self):
        x = np.array([
            [4.0, 4.0, 4.0],
        ])

        actual = normalize(x)

        np.testing.assert_allclose(
            actual,
            np.array([[0.0, 0.0, 0.0]]),
        )

    def test_bucketize_boundary(self):
        normalized = np.array([
            [0.0, 0.25, 0.5, 0.75, 1.0],
        ])

        actual = bucketize(normalized, 4)

        np.testing.assert_array_equal(
            actual,
            np.array([[0, 1, 2, 3, 3]]),
        )

    def test_row_score_ignores_nan(self):
        values = np.array([
            [1.0, np.nan, 3.0],
            [np.nan, np.nan, np.nan],
        ])

        score = row_score(values)

        self.assertAlmostEqual(score[0], 2.0)
        self.assertTrue(np.isnan(score[1]))


if __name__ == "__main__":
    unittest.main()
