import numpy as np

from .records import Observation, LeafStats
from .transforms import active_values, normalize, bucketize, row_score


class FeatureBuilder:
    def __init__(self, bucket_count: int):
        self.bucket_count = bucket_count

    def build(self, observation: Observation) -> LeafStats:
        selected = active_values(observation.values, observation.active)

        if selected.size == 0:
            normalized = np.empty((0, observation.values.shape[1]), dtype=float)
            bins = np.empty_like(normalized, dtype=int)
            score = np.nan
            return LeafStats(observation.name, normalized, bins, score)

        normalized = normalize(selected)
        bins = bucketize(normalized, self.bucket_count)
        score = float(np.min(row_score(normalized)))

        return LeafStats(
            name=observation.name,
            normalized=normalized,
            bins=bins,
            score=score,
        )
