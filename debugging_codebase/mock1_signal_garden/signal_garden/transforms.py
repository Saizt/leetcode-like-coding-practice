import numpy as np


def active_values(values: np.ndarray, active: np.ndarray) -> np.ndarray:
    """
    Return only entries whose activity mask is true.
    """
    return values[np.nonzero(active)]


def normalize(values: np.ndarray) -> np.ndarray:
    """
    Normalize each row independently into [0, 1].

    Constant rows are expected to become all zeros.
    """
    row_min = np.min(values, axis=1)
    row_max = np.max(values, axis=1)
    scale = row_max - row_min
    return (values - row_min) / scale


def bucketize(values: np.ndarray, bucket_count: int) -> np.ndarray:
    """
    Convert normalized [0, 1] values into integer bucket IDs
    in the range [0, bucket_count - 1].
    """
    scaled = (values * bucket_count).astype(int)
    return np.where(scaled == bucket_count, bucket_count - 1, scaled)


def row_score(values: np.ndarray) -> np.ndarray:
    """
    Compute one score per row using only non-NaN entries.
    Empty/all-NaN rows have score NaN.
    """
    valid = ~np.isnan(values)
    counts = np.sum(valid, axis=1)
    total = np.sum(np.where(valid, values, 0.0), axis=1)
    return total / counts
