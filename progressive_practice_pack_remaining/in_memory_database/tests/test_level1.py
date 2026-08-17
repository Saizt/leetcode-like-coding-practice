
import unittest
from database import InMemoryDatabase


class InMemoryDatabaseLevel1Test(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDatabase()

    def test_set_and_get(self):
        self.db.set("user1", "age", 30)
        self.assertEqual(self.db.get("user1", "age"), 30)

    def test_set_overwrites_field(self):
        self.db.set("user1", "age", 30)
        self.db.set("user1", "age", 31)
        self.assertEqual(self.db.get("user1", "age"), 31)

    def test_multiple_fields(self):
        self.db.set("user1", "age", 30)
        self.db.set("user1", "score", 100)
        self.assertEqual(self.db.get("user1", "age"), 30)
        self.assertEqual(self.db.get("user1", "score"), 100)

    def test_missing_key_or_field(self):
        self.assertIsNone(self.db.get("missing", "age"))
        self.db.set("user1", "age", 30)
        self.assertIsNone(self.db.get("user1", "missing"))

    def test_delete_existing_field(self):
        self.db.set("user1", "age", 30)
        self.assertTrue(self.db.delete("user1", "age"))
        self.assertIsNone(self.db.get("user1", "age"))

    def test_delete_missing_field(self):
        self.assertFalse(self.db.delete("missing", "age"))
        self.db.set("user1", "age", 30)
        self.assertFalse(self.db.delete("user1", "score"))


if __name__ == "__main__":
    unittest.main()
