import numpy as np
from models import RowStats


def batch_stats(values: np.ndarray) -> list[RowStats]:
    """
    Return one RowStats object per row.
    """
    result = []
    for row in values:
        result.append(
            RowStats(
                minimum=np.min(row),
                maximum=np.max(row),
                total=np.sum(row),
            )
        )
    return result
