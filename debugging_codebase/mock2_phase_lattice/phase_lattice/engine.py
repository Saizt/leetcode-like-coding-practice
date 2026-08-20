from .nodes import weave, terminal_payloads
from .prepare import FramePreparer
from .reporting import Reporter

class LatticeEngine:
    def __init__(self, channel_count=5):
        self.preparer = FramePreparer(channel_count)
        self.reporter = Reporter(channel_count)

    def execute(self, frames):
        root = weave(frames)
        ordered = terminal_payloads(root)
        prepared = [self.preparer.prepare(frame) for frame in ordered]
        return self.reporter.build(prepared)
