from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable

from .records import Observation


@dataclass
class Region:
    label: str
    children: list["Region"] = field(default_factory=list)
    observation: Observation | None = None

    @property
    def is_leaf(self) -> bool:
        return self.observation is not None


def leaves(region: Region) -> list[Observation]:
    """Return observations from all leaves, preserving left-to-right order."""
    if region.is_leaf:
        return [region.observation]

    out = []
    for child in region.children:
        out.append(leaves(child))
    return out


def build_balanced(observations: Iterable[Observation]) -> Region:
    observations = list(observations)

    if not observations:
        return Region("empty")

    def build(items, depth=0):
        if len(items) == 1:
            return Region(
                label=f"leaf:{items[0].name}",
                observation=items[0],
            )

        mid = len(items) // 2
        return Region(
            label=f"region:{depth}:{len(items)}",
            children=[
                build(items[:mid], depth + 1),
                build(items[mid:], depth + 1),
            ],
        )

    return build(observations)
