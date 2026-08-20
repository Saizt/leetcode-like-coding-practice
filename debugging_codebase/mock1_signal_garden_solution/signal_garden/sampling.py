import numpy as np


class Sampler:
    """
    Small helper used by callers to produce deterministic masks.
    """

    def __init__(self, rng: np.random.RandomState):
        self.rng = rng

    def mask(self, rows: int, keep_probability: float) -> np.ndarray:
        # One boolean flag per row.
        return self.rng.rand(rows) < keep_probability
