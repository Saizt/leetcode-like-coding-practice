import numpy as np
from .records import PreparedFrame
from .mathops import enabled_rows, calibrate_rows, classify, confidence_per_row

class FramePreparer:
    def __init__(self, channel_count):
        self.channel_count = channel_count

    def prepare(self, frame):
        selected = enabled_rows(frame.samples, frame.enabled)

        if selected.size == 0:
            width = frame.samples.shape[1]
            empty_float = np.empty((0, width), dtype=float)
            empty_int = np.empty((0, width), dtype=int)
            return PreparedFrame(frame.key, empty_float, empty_int, np.nan)

        calibrated = calibrate_rows(selected)
        channels = classify(calibrated, self.channel_count)
        confidence = float(np.max(confidence_per_row(calibrated)))
        return PreparedFrame(frame.key, calibrated, channels, confidence)
