import unittest
from cloud_storage import CloudStorage


class CloudStorageLevel4Test(unittest.TestCase):

    def setUp(self):
        self.storage = CloudStorage()
        self.storage.add_user("alice", 500)
        self.storage.add_user("bob", 400)

    def test_backup_user(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.add_file_by(
            "alice",
            "/alice/b.txt",
            150,
        )
        self.assertEqual(
            self.storage.backup_user("alice"),
            2,
        )

    def test_backup_missing_user(self):
        self.assertIsNone(
            self.storage.backup_user("ghost")
        )

    def test_empty_backup(self):
        self.assertEqual(
            self.storage.backup_user("alice"),
            0,
        )

    def test_backup_does_not_include_system_files(self):
        self.storage.add_file(
            "/system.dat",
            100,
        )
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.assertEqual(
            self.storage.backup_user("alice"),
            1,
        )

    def test_restore_deleted_file(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file(
            "/alice/a.txt"
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            1,
        )
        self.assertEqual(
            self.storage.get_file_size("/alice/a.txt"),
            100,
        )

    def test_restore_removes_files_created_after_backup(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.add_file_by(
            "alice",
            "/alice/new.txt",
            200,
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            1,
        )
        self.assertEqual(
            self.storage.get_file_size("/alice/a.txt"),
            100,
        )
        self.assertIsNone(
            self.storage.get_file_size("/alice/new.txt")
        )

    def test_restore_correctly_updates_capacity(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.add_file_by(
            "alice",
            "/alice/b.txt",
            150,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file("/alice/a.txt")
        self.storage.delete_file("/alice/b.txt")
        self.storage.restore_user("alice")
        self.assertEqual(
            self.storage.add_file_by(
                "alice",
                "/alice/c.txt",
                250,
            ),
            0,
        )

    def test_restore_skips_conflicting_file(self):
        self.storage.add_file_by(
            "alice",
            "/shared.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file(
            "/shared.txt"
        )
        self.storage.add_file_by(
            "bob",
            "/shared.txt",
            50,
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            0,
        )
        self.assertEqual(
            self.storage.get_file_size("/shared.txt"),
            50,
        )

    def test_restore_skips_system_file_conflict(self):
        self.storage.add_file_by(
            "alice",
            "/shared.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file(
            "/shared.txt"
        )
        self.storage.add_file(
            "/shared.txt",
            999,
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            0,
        )
        self.assertEqual(
            self.storage.get_file_size("/shared.txt"),
            999,
        )

    def test_backup_is_snapshot(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.add_file_by(
            "alice",
            "/alice/b.txt",
            100,
        )
        self.storage.delete_file(
            "/alice/a.txt"
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            1,
        )
        self.assertEqual(
            self.storage.get_file_size("/alice/a.txt"),
            100,
        )
        self.assertIsNone(
            self.storage.get_file_size("/alice/b.txt")
        )

    def test_new_backup_replaces_old_backup(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file(
            "/alice/a.txt"
        )
        self.storage.add_file_by(
            "alice",
            "/alice/b.txt",
            150,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file(
            "/alice/b.txt"
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            1,
        )
        self.assertIsNone(
            self.storage.get_file_size("/alice/a.txt")
        )
        self.assertEqual(
            self.storage.get_file_size("/alice/b.txt"),
            150,
        )

    def test_restore_without_backup_removes_current_files(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.add_file_by(
            "alice",
            "/alice/b.txt",
            150,
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            0,
        )
        self.assertIsNone(
            self.storage.get_file_size("/alice/a.txt")
        )
        self.assertIsNone(
            self.storage.get_file_size("/alice/b.txt")
        )
        self.assertEqual(
            self.storage.add_file_by(
                "alice",
                "/alice/full.bin",
                500,
            ),
            0,
        )

    def test_restore_missing_user(self):
        self.assertIsNone(
            self.storage.restore_user("ghost")
        )

    def test_source_backup_removed_after_merge(self):
        self.storage.add_file_by(
            "bob",
            "/bob/a.txt",
            100,
        )
        self.storage.backup_user("bob")
        self.storage.merge_users(
            "alice",
            "bob",
        )
        self.assertIsNone(
            self.storage.restore_user("bob")
        )

    def test_merge_does_not_change_target_backup(self):
        self.storage.add_file_by(
            "alice",
            "/alice/a.txt",
            100,
        )
        self.storage.backup_user("alice")
        self.storage.add_file_by(
            "bob",
            "/bob/b.txt",
            100,
        )
        self.storage.merge_users(
            "alice",
            "bob",
        )
        self.assertEqual(
            self.storage.restore_user("alice"),
            1,
        )
        self.assertEqual(
            self.storage.get_file_size("/alice/a.txt"),
            100,
        )
        self.assertIsNone(
            self.storage.get_file_size("/bob/b.txt")
        )

    def test_level2_search_after_restore(self):
        self.storage.add_file_by(
            "alice",
            "/docs/a.txt",
            100,
        )
        self.storage.add_file_by(
            "alice",
            "/docs/b.txt",
            200,
        )
        self.storage.backup_user("alice")
        self.storage.delete_file("/docs/a.txt")
        self.storage.delete_file("/docs/b.txt")
        self.storage.restore_user("alice")
        self.assertEqual(
            self.storage.find_file(
                "/docs",
                ".txt",
            ),
            [
                "/docs/b.txt(200)",
                "/docs/a.txt(100)",
            ],
        )


if __name__ == "__main__":
    unittest.main()