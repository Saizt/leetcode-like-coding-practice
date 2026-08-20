import unittest, numpy as np
from phase_lattice.reporting import Reporter
from phase_lattice.records import PreparedFrame

class ReportingTests(unittest.TestCase):
    def test_missing_confidences_are_counted(self):
        frames = [
            PreparedFrame("a", np.empty((0,3)), np.empty((0,3), dtype=int), np.nan),
            PreparedFrame("b", np.array([[0.,.5,1.]]), np.array([[0,2,4]]), .5),
        ]
        report = Reporter(5).build(frames)
        self.assertEqual(report.missing_count, 1)

    def test_histogram_uses_all_channels(self):
        frames = [
            PreparedFrame("a", np.zeros((1,4)), np.array([[0,1,1,4]]), .2)
        ]
        report = Reporter(5).build(frames)
        np.testing.assert_array_equal(
            report.channel_counts,
            np.array([1,2,0,0,1])
        )

if __name__ == "__main__":
    unittest.main()
