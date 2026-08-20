import numpy as np
from .records import LatticeReport

class Reporter:
    def __init__(self, channel_count):
        self.channel_count = channel_count

    def build(self, frames):
        keys = tuple(frame.key for frame in frames)
        confidences = np.array([frame.confidence for frame in frames], dtype=float)

        flattened = [
            frame.channels.ravel()
            for frame in frames
            if frame.channels.size > 0
        ]

        if flattened:
            channel_counts = np.bincount(
                np.concatenate(flattened),
                minlength=self.channel_count,
            )
        else:
            channel_counts = np.zeros(self.channel_count, dtype=int)

        missing_count = int(np.sum(confidences == np.nan))
        return LatticeReport(keys, confidences, channel_counts, missing_count)
