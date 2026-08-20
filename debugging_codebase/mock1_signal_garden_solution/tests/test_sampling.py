import unittest
import numpy as np

from signal_garden.sampling import Sampler


class SamplingTests(unittest.TestCase):
    def test_sampler_uses_supplied_random_state(self):
        rng1 = np.random.RandomState(123)
        rng2 = np.random.RandomState(123)

        sampler1 = Sampler(rng1)
        sampler2 = Sampler(rng2)
        
        np.testing.assert_array_equal(
            sampler1.mask(20, 0.5),
            sampler2.mask(20, 0.5),
        )

    def test_sampler_advances_its_own_state(self):
        rng = np.random.RandomState(7)
        sampler = Sampler(rng)

        first = sampler.mask(100, 0.5)
        second = sampler.mask(100, 0.5)

        self.assertFalse(np.array_equal(first, second))


if __name__ == "__main__":
    unittest.main()
