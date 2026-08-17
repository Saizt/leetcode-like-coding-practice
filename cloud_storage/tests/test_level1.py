import unittest
from cloud_storage import CloudStorage


class CloudStorageLevel1Test(unittest.TestCase):

    def setUp(self):
        self.storage = CloudStorage()

    def test_add_file(self):
        self.assertTrue(self.storage.add_file("/docs/report.pdf", 120))
        self.assertEqual(self.storage.get_file_size("/docs/report.pdf"), 120)

    def test_cannot_add_duplicate_file(self):
        self.assertTrue(self.storage.add_file("/docs/report.pdf", 120))
        self.assertFalse(self.storage.add_file("/docs/report.pdf", 999))
        self.assertEqual(self.storage.get_file_size("/docs/report.pdf"), 120)

    def test_get_missing_file(self):
        self.assertIsNone(self.storage.get_file_size("/missing.txt"))

    def test_delete_file(self):
        self.storage.add_file("/images/photo.png", 250)
        self.assertEqual(self.storage.delete_file("/images/photo.png"), 250)
        self.assertIsNone(self.storage.get_file_size("/images/photo.png"))

    def test_delete_missing_file(self):
        self.assertIsNone(self.storage.delete_file("/missing.txt"))

    def test_files_with_different_names_are_independent(self):
        self.storage.add_file("/a.txt", 10)
        self.storage.add_file("/b.txt", 20)
        self.assertEqual(self.storage.get_file_size("/a.txt"), 10)
        self.assertEqual(self.storage.get_file_size("/b.txt"), 20)


if __name__ == "__main__":
    unittest.main()