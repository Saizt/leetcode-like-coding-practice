import numpy as np


def masked_normalize(values: np.ndarray, mask: np.ndarray) -> np.ndarray:
    masked = np.where(mask, values, 0.0)
    totals = np.sum(masked, axis=1)
    return masked / totals
