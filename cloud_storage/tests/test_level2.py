import unittest
from cloud_storage import CloudStorage


class CloudStorageLevel2Test(unittest.TestCase):

    def setUp(self):
        self.storage = CloudStorage()
        self.storage.add_file("/docs/report.txt", 100)
        self.storage.add_file("/docs/notes.txt", 50)
        self.storage.add_file("/docs/archive/report.txt", 200)
        self.storage.add_file("/images/photo.png", 300)
        self.storage.add_file("/images/icon.png", 50)

    def test_find_by_prefix_and_suffix(self):
        self.assertEqual(
            self.storage.find_file("/docs", ".txt"),
            [
                "/docs/archive/report.txt(200)",
                "/docs/report.txt(100)",
                "/docs/notes.txt(50)",
            ],
        )

    def test_find_with_different_suffix(self):
        self.assertEqual(
            self.storage.find_file("/images", ".png"),
            [
                "/images/photo.png(300)",
                "/images/icon.png(50)",
            ],
        )

    def test_file_must_match_both_conditions(self):
        self.assertEqual(
            self.storage.find_file("/docs", "report.txt"),
            [
                "/docs/archive/report.txt(200)",
                "/docs/report.txt(100)",
            ],
        )

    def test_equal_sizes_use_lexicographical_order(self):
        self.storage.add_file("/same/z.txt", 100)
        self.storage.add_file("/same/a.txt", 100)
        self.storage.add_file("/same/m.txt", 100)
        self.assertEqual(
            self.storage.find_file("/same", ".txt"),
            [
                "/same/a.txt(100)",
                "/same/m.txt(100)",
                "/same/z.txt(100)",
            ],
        )

    def test_no_matching_files(self):
        self.assertEqual(self.storage.find_file("/videos", ".mp4"), [])

    def test_search_does_not_modify_storage(self):
        self.storage.find_file("/docs", ".txt")
        self.assertEqual(self.storage.get_file_size("/docs/report.txt"), 100)
        self.assertEqual(self.storage.get_file_size("/images/photo.png"), 300)


if __name__ == "__main__":
    unittest.main()