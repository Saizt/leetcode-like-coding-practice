import unittest

from signal_garden.tree import build_balanced, leaves
from tests.fixtures import basic_observations


class TreeTests(unittest.TestCase):
    def test_recursive_leaf_order_is_preserved(self):
        observations = basic_observations()
        tree = build_balanced(observations)

        result = leaves(tree)

        self.assertEqual(
            [item.name for item in result],
            ["north", "south", "west"],
        )

    def test_single_leaf(self):
        observation = basic_observations()[0]

        result = leaves(build_balanced([observation]))

        self.assertEqual(result, [observation])


if __name__ == "__main__":
    unittest.main()
