import unittest
from phase_lattice.nodes import weave, terminal_payloads
from tests.helpers import standard_frames

class NodeTests(unittest.TestCase):
    def test_terminal_payloads_are_flat_and_ordered(self):
        frames = standard_frames()
        result = terminal_payloads(weave(frames))
        self.assertEqual([x.key for x in result], ["alpha","beta","gamma"])

    def test_single_payload(self):
        f = standard_frames()[0]
        self.assertEqual(terminal_payloads(weave([f])), [f])

if __name__ == "__main__":
    unittest.main()
