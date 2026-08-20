import unittest
import numpy as np

from signal_garden import GardenEngine
from tests.fixtures import basic_observations, obs


class PipelineTests(unittest.TestCase):
    def test_report_preserves_observation_order(self):
        report = GardenEngine(bucket_count=4).run(
            basic_observations()
        )

        self.assertEqual(
            report.names,
            ("north", "south", "west"),
        )

    def test_empty_observation_is_reported_as_invalid(self):
        report = GardenEngine(bucket_count=4).run(
            basic_observations()
        )

        self.assertEqual(report.invalid_count, 1)
        self.assertTrue(np.isnan(report.scores[-1]))

    def test_histogram_contains_only_active_rows(self):
        report = GardenEngine(bucket_count=4).run(
            basic_observations()
        )

        expected = np.array([6, 0, 3, 3])

        np.testing.assert_array_equal(
            report.histogram,
            expected,
        )

    def test_masked_rows_are_ignored(self):
        observation = obs(
            "masked",
            [
                [1.0, 2.0, 3.0],
                [1000.0, 2000.0, 3000.0],
            ],
            [True, False],
        )

        report = GardenEngine(bucket_count=4).run([observation])

        self.assertEqual(report.names, ("masked",))
        np.testing.assert_array_equal(
            report.histogram,
            np.array([1, 0, 1, 1]),
        )

    def test_all_masked_observation_does_not_crash(self):
        observation = obs(
            "none",
            [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
            ],
            [False, False],
        )

        report = GardenEngine(bucket_count=4).run([observation])

        self.assertEqual(report.invalid_count, 1)
        self.assertEqual(report.histogram.tolist(), [0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
