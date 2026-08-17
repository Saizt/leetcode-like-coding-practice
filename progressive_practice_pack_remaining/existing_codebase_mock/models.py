from collections import NamedTuple
from typing import Tuple


class RowStats(NamedTuple):
    minimum: float
    maximum: float
    total: float


class Request(NamedTuple):
    name: str
    children: Tuple["Request", ...] = ()


class SampleResult(NamedTuple):
    indices: tuple[int, ...]
