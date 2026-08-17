import unittest
from cloud_storage import CloudStorage


class CloudStorageLevel3Test(unittest.TestCase):

    def setUp(self):
        self.storage = CloudStorage()
        self.storage.add_user("alice", 500)
        self.storage.add_user("bob", 300)

    def test_add_user(self):
        self.assertTrue(self.storage.add_user("charlie", 200))
        self.assertFalse(self.storage.add_user("charlie", 1000))

    def test_add_file_by_user(self):
        self.assertEqual(
            self.storage.add_file_by("alice", "/alice/a.txt", 120),
            380,
        )
        self.assertEqual(self.storage.get_file_size("/alice/a.txt"), 120)

    def test_add_file_by_missing_user(self):
        self.assertIsNone(self.storage.add_file_by("ghost", "/ghost/a.txt", 100))

    def test_cannot_exceed_capacity(self):
        self.assertIsNone(self.storage.add_file_by("bob", "/bob/large.bin", 400))
        self.assertIsNone(self.storage.get_file_size("/bob/large.bin"))

    def test_duplicate_file_name_fails(self):
        self.storage.add_file("/shared.txt", 50)
        self.assertIsNone(self.storage.add_file_by("alice", "/shared.txt", 100))

    def test_delete_restores_capacity(self):
        self.storage.add_file_by("alice", "/alice/a.txt", 120)
        self.assertEqual(self.storage.delete_file("/alice/a.txt"), 120)
        self.assertEqual(
            self.storage.add_file_by("alice", "/alice/b.txt", 500),
            0,
        )

    def test_delete_system_file_does_not_affect_users(self):
        self.storage.add_file("/system.dat", 100)
        self.storage.delete_file("/system.dat")
        self.assertEqual(
            self.storage.add_file_by("alice", "/alice/full.bin", 500),
            0,
        )

    def test_merge_users(self):
        self.storage.add_file_by("alice", "/alice/a.txt", 100)
        self.storage.add_file_by("bob", "/bob/b.txt", 50)
        remaining = self.storage.merge_users("alice", "bob")
        self.assertEqual(remaining, 650)

    def test_source_user_removed_after_merge(self):
        self.storage.merge_users("alice", "bob")
        self.assertIsNone(self.storage.add_file_by("bob", "/bob/new.txt", 10))

    def test_files_follow_merged_user(self):
        self.storage.add_file_by("bob", "/bob/a.txt", 100)
        self.storage.merge_users("alice", "bob")
        self.storage.delete_file("/bob/a.txt")
        self.assertEqual(
            self.storage.add_file_by("alice", "/alice/full.bin", 800),
            0,
        )

    def test_cannot_merge_same_user(self):
        self.assertIsNone(
            self.storage.merge_users("alice", "alice")
        )

    def test_cannot_merge_missing_user(self):
        self.assertIsNone(
            self.storage.merge_users("alice", "ghost")
        )

    def test_level2_search_still_works_for_user_files(self):
        self.storage.add_file_by("alice", "/docs/b.txt", 100)
        self.storage.add_file_by("bob", "/docs/a.txt", 100)
        self.assertEqual(
            self.storage.find_file("/docs", ".txt"),
            ["/docs/a.txt(100)", "/docs/b.txt(100)"]
        )


if __name__ == "__main__":
    unittest.main()