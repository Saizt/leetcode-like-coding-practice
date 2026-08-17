import numpy as np
from models import SampleResult


def sample_rows(probabilities: np.ndarray, seed: int) -> SampleResult:
    rng = np.random.RandomState(seed)
    indices = []

    for row in probabilities:
        indices.append(rng.choice(len(row), p=row))

    return SampleResult(tuple(indices))
