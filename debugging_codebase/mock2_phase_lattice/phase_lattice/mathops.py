import numpy as np

def enabled_rows(samples, enabled):
    indices = np.where(enabled)
    return samples[indices]

def calibrate_rows(samples):
    low = np.min(samples, axis=1)
    high = np.max(samples, axis=1)
    span = high - low
    return (samples - low) / span

def classify(calibrated, channels):
    raw = (calibrated * channels).astype(int)
    return np.where(raw >= channels, channels - 1, raw)

def confidence_per_row(calibrated):
    valid = ~np.isnan(calibrated)
    total = np.sum(np.where(valid, calibrated, 0.0), axis=1)
    count = np.sum(valid, axis=1)
    return total / count
