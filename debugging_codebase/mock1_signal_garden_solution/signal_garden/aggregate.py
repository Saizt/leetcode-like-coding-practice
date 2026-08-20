import numpy as np

from .records import LeafStats, GardenReport


class ReportAggregator:
    def __init__(self, bucket_count: int):
        self.bucket_count = bucket_count

    def aggregate(self, stats: list[LeafStats]) -> GardenReport:
        names = tuple(item.name for item in stats)
        scores = np.array([item.score for item in stats], dtype=float)

        all_bins = [
            item.bins.reshape(-1)
            for item in stats
            if item.bins.size
        ]

        if all_bins:
            histogram = np.bincount(
                np.concatenate(all_bins),
                minlength=self.bucket_count,
            )
        else:
            histogram = np.zeros(self.bucket_count, dtype=int)

        invalid_count = int(np.sum(np.isnan(scores)))

        return GardenReport(
            names=names,
            scores=scores,
            histogram=histogram,
            invalid_count=invalid_count,
        )
