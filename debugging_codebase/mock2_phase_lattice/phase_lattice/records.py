from typing import NamedTuple
import numpy as np

class Frame(NamedTuple):
    key: str
    samples: np.ndarray
    enabled: np.ndarray

class PreparedFrame(NamedTuple):
    key: str
    calibrated: np.ndarray
    channels: np.ndarray
    confidence: float

class LatticeReport(NamedTuple):
    keys: tuple[str, ...]
    confidences: np.ndarray
    channel_counts: np.ndarray
    missing_count: int
