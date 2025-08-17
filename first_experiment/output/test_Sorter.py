import os
import shutil
import unittest
from unittest.mock import patch

class Sorter:
    def __init__(self, directory: str, extensions: list):
        self.directory = directory
        self.extensions = [ext.lower() for ext in extensions]
        self.sorted_count = 0
        self.unsorted_count = 0

    def sort_files(self):
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"The directory '{self.directory}' does not exist.")
        files = os.listdir(self.directory)
        if not files:
            raise ValueError(f"The directory '{self.directory}' is empty.")
        for file in files:
            self._move_file(file)
        return self.sorted_count, self.unsorted_count

    def _move_file(self, file: str):
        source = os.path.join(self.directory, file)
        if os.path.isfile(source):
            name, ext = os.path.splitext(file)
            ext = ext[1:].lower()
            if ext in self.extensions:
                target_dir = os.path.join(self.directory, ext)
                self._create_directory(target_dir)
                self._move(source, target_dir, file)
            elif ext == "":
                self._handle_no_extension(source, name)
            else:
                self.unsorted_count += 1

    def _handle_no_extension(self, source: str, name: str):
        no_extension_dir = os.path.join(self.directory, 'no_extension')
        self._create_directory(no_extension_dir)
        self._move(source, no_extension_dir, name)

    def _move(self, source: str, target_dir: str, filename: str):
        try:
            shutil.move(source, os.path.join(target_dir, filename))
            self.sorted_count += 1
        except Exception:
            self.unsorted_count += 1

    def _create_directory(self, target_dir: str):
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

class TestSorter(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_sort_files_success(self, mock_move, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['file1.txt', 'file2.txt', 'file3.doc']
        sorter = Sorter('/test/directory', ['txt', 'doc'])
        sorted_count, unsorted_count = sorter.sort_files()
        self.assertEqual(sorted_count, 3)
        self.assertEqual(unsorted_count, 0)

    @patch('os.listdir')
    @patch('os.path.exists')
    def test_sort_files_empty_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        sorter = Sorter('/test/directory', ['txt', 'doc'])
        with self.assertRaises(ValueError):
            sorter.sort_files()

    @patch('os.listdir')
    @patch('os.path.exists')
    def test_sort_files_non_existing_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = False
        sorter = Sorter('/test/directory', ['txt', 'doc'])
        with self.assertRaises(FileNotFoundError):
            sorter.sort_files()

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_move_file_with_no_extension(self, mock_move, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True
        mock_listdir.return_value = ['file1', 'file2.txt']
        sorter = Sorter('/test/directory', ['txt'])
        sorted_count, unsorted_count = sorter.sort_files()
        self.assertEqual(sorted_count, 1)
        self.assertEqual(unsorted_count, 1)

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_move_file_error(self, mock_move, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['file1.txt']
        mock_move.side_effect = Exception('Move failed')
        sorter = Sorter('/test/directory', ['txt'])
        sorted_count, unsorted_count = sorter.sort_files()
        self.assertEqual(sorted_count, 0)
        self.assertEqual(unsorted_count, 1)

if __name__ == '__main__':
    unittest.main()