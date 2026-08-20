import numpy as np

class SelectionPolicy:
    def __init__(self, rng):
        self.rng = rng

    def choose(self, count, probability):
        return np.random.rand(count) < probability

class ThresholdPolicy(SelectionPolicy):
    def __init__(self, rng, floor):
        self.floor = floor

    def choose(self, count, probability):
        base = super().choose(count, probability)
        return np.where(probability >= self.floor, base, False)
