import unittest, numpy as np
from phase_lattice.mathops import enabled_rows, calibrate_rows, classify, confidence_per_row

class MathOpsTests(unittest.TestCase):
    def test_enabled_rows_filters_rows(self):
        samples = np.array([[1.,2.],[10.,20.],[100.,200.]])
        enabled = np.array([True,False,True])
        np.testing.assert_array_equal(
            enabled_rows(samples, enabled),
            np.array([[1.,2.],[100.,200.]])
        )

    def test_calibrate_rows(self):
        samples = np.array([[1.,2.,3.],[10.,20.,30.]])
        np.testing.assert_allclose(
            calibrate_rows(samples),
            np.array([[0.,.5,1.],[0.,.5,1.]])
        )

    def test_constant_rows_become_zero(self):
        samples = np.array([[7.,7.,7.]])
        np.testing.assert_allclose(
            calibrate_rows(samples),
            np.array([[0.,0.,0.]])
        )

    def test_classify_upper_boundary(self):
        calibrated = np.array([[0.,.2,.4,.8,1.]])
        np.testing.assert_array_equal(
            classify(calibrated, 5),
            np.array([[0,1,2,4,4]])
        )

    def test_confidence_ignores_nan(self):
        x = np.array([[0.,np.nan,1.],[np.nan,np.nan,np.nan]])
        r = confidence_per_row(x)
        self.assertAlmostEqual(r[0], .5)
        self.assertTrue(np.isnan(r[1]))

if __name__ == "__main__":
    unittest.main()
