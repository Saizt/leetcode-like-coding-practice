from typing import NamedTuple
import numpy as np


class Observation(NamedTuple):
    name: str
    values: np.ndarray
    active: np.ndarray


class LeafStats(NamedTuple):
    name: str
    normalized: np.ndarray
    bins: np.ndarray
    score: float


class GardenReport(NamedTuple):
    names: tuple[str, ...]
    scores: np.ndarray
    histogram: np.ndarray
    invalid_count: int
