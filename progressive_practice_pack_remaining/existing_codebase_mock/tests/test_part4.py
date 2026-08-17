import unittest

from models import Request
from requests import expand_leaves


class Part4Test(unittest.TestCase):

    def test_single_leaf(self):
        leaf = Request("a")
        self.assertEqual(expand_leaves(leaf), [leaf])

    def test_nested_depth_first_order(self):
        tree = Request(
            "root",
            (
                Request("a"),
                Request(
                    "branch",
                    (
                        Request("b"),
                        Request(
                            "deep",
                            (
                                Request("c"),
                                Request("d"),
                            ),
                        ),
                    ),
                ),
                Request("e"),
            ),
        )

        self.assertEqual(
            [r.name for r in expand_leaves(tree)],
            ["a", "b", "c", "d", "e"],
        )

    def test_each_leaf_once(self):
        tree = Request(
            "root",
            (
                Request("a"),
                Request("b"),
                Request("c"),
            ),
        )

        self.assertEqual(
            [r.name for r in expand_leaves(tree)],
            ["a", "b", "c"],
        )


if __name__ == "__main__":
    unittest.main()
