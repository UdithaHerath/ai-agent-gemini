import unittest
from tools.file_reader_tool import FileReaderTool


class TestFileReaderTool(unittest.TestCase):

    def setUp(self):
        self.reader = FileReaderTool()

    def test_read_existing_file(self):
        result = self.reader.execute({"file_path": "sample.txt"})
        self.assertTrue(len(result) > 0)

    def test_file_not_found(self):
        result = self.reader.execute({"file_path": "nonexistent.txt"})
        self.assertTrue("error" in result.lower() or "not found" in result.lower())


if __name__ == "__main__":
    unittest.main()