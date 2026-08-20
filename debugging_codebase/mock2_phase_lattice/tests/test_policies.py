import unittest, numpy as np
from phase_lattice.policies import SelectionPolicy, ThresholdPolicy

class PolicyTests(unittest.TestCase):
    def test_selection_policy_uses_supplied_rng(self):
        p1 = SelectionPolicy(np.random.RandomState(99))
        p2 = SelectionPolicy(np.random.RandomState(99))
        np.testing.assert_array_equal(p1.choose(50,.4), p2.choose(50,.4))

    def test_threshold_policy_preserves_rng_behavior(self):
        p1 = ThresholdPolicy(np.random.RandomState(17), floor=.2)
        p2 = ThresholdPolicy(np.random.RandomState(17), floor=.2)
        np.testing.assert_array_equal(p1.choose(50,.8), p2.choose(50,.8))

    def test_threshold_below_floor_returns_false_mask(self):
        p = ThresholdPolicy(np.random.RandomState(5), floor=.7)
        np.testing.assert_array_equal(
            p.choose(20,.4),
            np.zeros(20, dtype=bool)
        )

if __name__ == "__main__":
    unittest.main()
