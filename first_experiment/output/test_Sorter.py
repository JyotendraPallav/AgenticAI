import os
import unittest
from unittest.mock import patch, MagicMock
import shutil

from Sorter import Sorter

class TestSorter(unittest.TestCase):
    def setUp(self):
        self.directory = 'test_directory'
        self.extensions = ['txt', 'jpg', 'png']
        os.makedirs(self.directory, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.directory)

    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.move')
    @patch('os.makedirs')
    def test_sort_files(self, mock_makedirs, mock_move, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['file1.txt', 'file2.jpg', 'file3', 'file4.png', 'folder']  # contains a folder that should be ignored
        sorter = Sorter(self.directory, self.extensions)
        sorted_count, unsorted_count = sorter.sort_files()

        self.assertEqual(sorted_count, 3)
        self.assertEqual(unsorted_count, 1)
        self.assertEqual(sorter.get_summary()['sorted_count'], 3)
        self.assertEqual(sorter.get_summary()['no_extension_count'], 1)

    @patch('os.path.exists')
    def test_directory_not_exist(self, mock_exists):
        mock_exists.return_value = False
        sorter = Sorter(self.directory, self.extensions)
        with self.assertRaises(FileNotFoundError):
            sorter.sort_files()

    def test_get_file_extension(self):
        sorter = Sorter(self.directory, self.extensions)
        self.assertEqual(sorter._get_file_extension('file.txt'), 'txt')
        self.assertEqual(sorter._get_file_extension('file'), '')

if __name__ == '__main__':
    unittest.main()