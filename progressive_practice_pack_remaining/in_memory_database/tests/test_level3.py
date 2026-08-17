
import unittest
from database import InMemoryDatabase


class InMemoryDatabaseLevel3Test(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDatabase()

    def test_set_at_and_get_at(self):
        self.db.set_at("a", "x", 10, timestamp=1)
        self.assertEqual(self.db.get_at("a", "x", timestamp=1), 10)
        self.assertEqual(self.db.get_at("a", "x", timestamp=100), 10)

    def test_ttl_half_open_interval(self):
        self.db.set_at_with_ttl("a", "x", 10, timestamp=5, ttl=10)
        self.assertEqual(self.db.get_at("a", "x", timestamp=5), 10)
        self.assertEqual(self.db.get_at("a", "x", timestamp=14), 10)
        self.assertIsNone(self.db.get_at("a", "x", timestamp=15))

    def test_later_write_replaces_ttl(self):
        self.db.set_at_with_ttl("a", "x", 10, timestamp=5, ttl=10)
        self.db.set_at("a", "x", 20, timestamp=8)
        self.assertEqual(self.db.get_at("a", "x", timestamp=20), 20)

    def test_later_ttl_write_replaces_non_expiring_value(self):
        self.db.set_at("a", "x", 10, timestamp=1)
        self.db.set_at_with_ttl("a", "x", 20, timestamp=5, ttl=3)
        self.assertEqual(self.db.get_at("a", "x", timestamp=7), 20)
        self.assertIsNone(self.db.get_at("a", "x", timestamp=8))

    def test_delete_at(self):
        self.db.set_at("a", "x", 10, timestamp=1)
        self.assertTrue(self.db.delete_at("a", "x", timestamp=5))
        self.assertIsNone(self.db.get_at("a", "x", timestamp=5))

    def test_delete_expired_field_returns_false(self):
        self.db.set_at_with_ttl("a", "x", 10, timestamp=1, ttl=3)
        self.assertFalse(self.db.delete_at("a", "x", timestamp=4))

    def test_scan_at_excludes_expired_fields(self):
        self.db.set_at("a", "alive", 1, timestamp=1)
        self.db.set_at_with_ttl("a", "expired", 2, timestamp=1, ttl=5)

        self.assertEqual(
            self.db.scan_at("a", timestamp=6),
            ["alive(1)"],
        )

    def test_scan_by_prefix_at(self):
        self.db.set_at("a", "score", 100, timestamp=1)
        self.db.set_at_with_ttl("a", "status", 1, timestamp=1, ttl=5)
        self.db.set_at("a", "age", 30, timestamp=1)

        self.assertEqual(
            self.db.scan_by_prefix_at("a", "s", timestamp=3),
            ["score(100)", "status(1)"],
        )

        self.assertEqual(
            self.db.scan_by_prefix_at("a", "s", timestamp=6),
            ["score(100)"],
        )


if __name__ == "__main__":
    unittest.main()
