
import unittest
from database import InMemoryDatabase


class InMemoryDatabaseLevel4Test(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDatabase()

    def test_backup_returns_nonempty_record_count(self):
        self.db.set_at("a", "x", 1, timestamp=1)
        self.db.set_at("b", "y", 2, timestamp=1)
        self.assertEqual(self.db.backup(timestamp=5), 2)

    def test_backup_excludes_expired_fields(self):
        self.db.set_at_with_ttl("a", "x", 1, timestamp=1, ttl=3)
        self.assertEqual(self.db.backup(timestamp=5), 0)

    def test_restore_latest_backup_at_or_before_target(self):
        self.db.set_at("a", "x", 1, timestamp=1)
        self.db.backup(timestamp=5)

        self.db.set_at("a", "x", 2, timestamp=6)
        self.db.backup(timestamp=10)

        self.db.set_at("a", "x", 3, timestamp=11)

        self.db.restore(timestamp=20, restore_timestamp=7)
        self.assertEqual(self.db.get_at("a", "x", timestamp=20), 1)

    def test_restore_newer_backup(self):
        self.db.set_at("a", "x", 1, timestamp=1)
        self.db.backup(timestamp=5)

        self.db.set_at("a", "x", 2, timestamp=6)
        self.db.backup(timestamp=10)

        self.db.restore(timestamp=20, restore_timestamp=10)
        self.assertEqual(self.db.get_at("a", "x", timestamp=20), 2)

    def test_restore_without_backup_clears_database(self):
        self.db.set_at("a", "x", 1, timestamp=1)
        self.db.restore(timestamp=10, restore_timestamp=5)
        self.assertIsNone(self.db.get_at("a", "x", timestamp=10))

    def test_restore_preserves_remaining_ttl(self):
        self.db.set_at_with_ttl("a", "x", 10, timestamp=5, ttl=20)
        self.db.backup(timestamp=10)  # 15 units remain.

        self.db.restore(timestamp=100, restore_timestamp=10)

        self.assertEqual(self.db.get_at("a", "x", timestamp=114), 10)
        self.assertIsNone(self.db.get_at("a", "x", timestamp=115))

    def test_restore_preserves_non_expiring_fields(self):
        self.db.set_at("a", "x", 10, timestamp=1)
        self.db.backup(timestamp=5)

        self.db.restore(timestamp=100, restore_timestamp=5)

        self.assertEqual(self.db.get_at("a", "x", timestamp=1000), 10)

    def test_backup_is_immutable(self):
        self.db.set_at("a", "x", 1, timestamp=1)
        self.db.backup(timestamp=5)

        self.db.set_at("a", "x", 99, timestamp=6)
        self.db.restore(timestamp=20, restore_timestamp=5)

        self.assertEqual(self.db.get_at("a", "x", timestamp=20), 1)


if __name__ == "__main__":
    unittest.main()
