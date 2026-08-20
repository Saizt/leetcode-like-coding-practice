from __future__ import annotations
from dataclasses import dataclass, field
from .records import Frame

@dataclass
class Cell:
    name: str
    branches: list["Cell"] = field(default_factory=list)
    payload: Frame | None = None

    @property
    def terminal(self):
        return self.payload is not None

def weave(frames):
    frames = list(frames)
    if not frames:
        return Cell("empty")

    def build(items, depth=0):
        if len(items) == 1:
            return Cell(f"leaf:{items[0].key}", payload=items[0])
        pivot = (len(items) + 1) // 2
        return Cell(
            f"cell:{depth}:{len(items)}",
            branches=[
                build(items[:pivot], depth + 1),
                build(items[pivot:], depth + 1),
            ],
        )
    return build(frames)

def terminal_payloads(cell):
    if cell.terminal:
        return [cell.payload]

    result = []
    for branch in cell.branches:
        result += [terminal_payloads(branch)]
    return result
