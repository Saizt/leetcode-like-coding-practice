import numpy as np


def normalize_rows(x):
    breakpoint()
    row_min = np.min(x, axis=1).reshape(-1, 1)
    row_max = np.max(x, axis=1).reshape(-1, 1)

    res = (x - row_min) / (row_max - row_min)
    clean_res = np.nan_to_num(res)
    return clean_res


def prepare_batch(values):
    arr = np.array(values, dtype=float)
    return normalize_rows(arr)


def summarize(batch):
    return {
        "shape": batch.shape,
        "sum": np.sum(batch),
        "contains_nan": np.any(np.isnan(batch)),
    }


def pipeline(values):
    batch = prepare_batch(values)
    return summarize(batch)


if __name__ == "__main__":
    values = [
        [1.0, 2.0, 3.0],
        [10.0, 20.0, 30.0],
        [5.0, 5.0, 5.0]
    ]

    result = pipeline(values)

    print(result)

    assert result["shape"] == (2, 3) or result["shape"] == (3, 3)
    assert not result["contains_nan"]
    assert np.isclose(result["sum"], 3.0)