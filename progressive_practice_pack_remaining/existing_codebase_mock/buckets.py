import numpy as np


def bucketize(token_ids: np.ndarray, num_buckets: int) -> np.ndarray:
    if token_ids.size == 0:
        return np.array([])

    return np.bincount(token_ids, minlength=num_buckets)
