
import unittest
from database import InMemoryDatabase


class InMemoryDatabaseLevel2Test(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDatabase()
        self.db.set("user1", "age", 30)
        self.db.set("user1", "address", 100)
        self.db.set("user1", "score", 90)
        self.db.set("user1", "status", 1)

    def test_scan(self):
        self.assertEqual(
            self.db.scan("user1"),
            ["address(100)", "age(30)", "score(90)", "status(1)"],
        )

    def test_scan_missing_record(self):
        self.assertEqual(self.db.scan("missing"), [])

    def test_scan_by_prefix(self):
        self.assertEqual(
            self.db.scan_by_prefix("user1", "s"),
            ["score(90)", "status(1)"],
        )

    def test_scan_by_prefix_single_match(self):
        self.assertEqual(
            self.db.scan_by_prefix("user1", "add"),
            ["address(100)"],
        )

    def test_scan_by_prefix_no_match(self):
        self.assertEqual(
            self.db.scan_by_prefix("user1", "zzz"),
            [],
        )

    def test_delete_reflected_in_scan(self):
        self.db.delete("user1", "age")
        self.assertEqual(
            self.db.scan("user1"),
            ["address(100)", "score(90)", "status(1)"],
        )


if __name__ == "__main__":
    unittest.main()
