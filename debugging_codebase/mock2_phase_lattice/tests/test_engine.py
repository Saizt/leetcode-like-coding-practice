import unittest, numpy as np
from phase_lattice import LatticeEngine
from tests.helpers import frame, standard_frames

class EngineTests(unittest.TestCase):
    def test_keys_preserve_input_order(self):
        report = LatticeEngine(5).execute(standard_frames())
        self.assertEqual(report.keys, ("alpha","beta","gamma"))

    def test_all_disabled_frame_is_missing(self):
        report = LatticeEngine(5).execute(standard_frames())
        self.assertEqual(report.missing_count, 1)
        self.assertTrue(np.isnan(report.confidences[-1]))

    def test_inactive_rows_do_not_contribute(self):
        only = frame(
            "delta",
            [[0,1,2,3],[100,200,300,400]],
            [True,False]
        )
        report = LatticeEngine(5).execute([only])
        np.testing.assert_array_equal(
            report.channel_counts,
            np.array([1,1,1,0,1])
        )

    def test_engine_handles_single_frame(self):
        only = standard_frames()[0]
        report = LatticeEngine(5).execute([only])
        self.assertEqual(report.keys, ("alpha",))
        self.assertEqual(report.missing_count, 0)

if __name__ == "__main__":
    unittest.main()
