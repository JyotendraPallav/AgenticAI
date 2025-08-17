import os
import shutil

class Sorter:
    def __init__(self, directory: str, extensions: list):
        """
        Initialize the Sorter with a directory and a list of file extensions.
        
        :param directory: The path of the directory containing files to be sorted.
        :param extensions: A list of file extensions to sort the files by.
        """
        self.directory = directory
        self.extensions = [ext.lower() for ext in extensions]  # Convert all extensions to lower case
        self.sorted_count = 0
        self.unsorted_count = 0

    def sort_files(self):
        """
        Sort files in the specified directory based on the file extensions.
        It creates subdirectories for each file extension and moves files accordingly.
        It also handles various edge cases such as empty or non-existing directories.
        
        :return: A tuple of (number of files sorted, number of files that could not be sorted)
        """
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"The directory '{self.directory}' does not exist.")

        files = os.listdir(self.directory)
        if not files:
            raise ValueError(f"The directory '{self.directory}' is empty.")

        for file in files:
            self._move_file(file)

        return self.sorted_count, self.unsorted_count

    def _move_file(self, file: str):
        """
        Move a single file to its corresponding subdirectory based on its extension.
        
        :param file: The file name to be sorted.
        """
        source = os.path.join(self.directory, file)
        if os.path.isfile(source):
            name, ext = os.path.splitext(file)
            ext = ext[1:].lower()  # Get the extension without the dot and to lower case
            
            if ext in self.extensions:
                target_dir = os.path.join(self.directory, ext)
                self._create_directory(target_dir)
                self._move(source, target_dir, file)
            elif ext == "":
                self._handle_no_extension(source, name)
            else:
                self.unsorted_count += 1

    def _handle_no_extension(self, source: str, name: str):
        """
        Handle files with no extension by moving them to 'no_extension' directory.
        
        :param source: The source path of the file with no extension.
        :param name: The name of the file.
        """
        no_extension_dir = os.path.join(self.directory, 'no_extension')
        self._create_directory(no_extension_dir)
        self._move(source, no_extension_dir, name)
    
    def _move(self, source: str, target_dir: str, filename: str):
        """
        Move a file to the target directory.
        
        :param source: The source path of the file.
        :param target_dir: The destination directory where the file needs to be moved.
        :param filename: The name of the file being moved.
        """
        try:
            shutil.move(source, os.path.join(target_dir, filename))
            self.sorted_count += 1
        except Exception as e:
            self.unsorted_count += 1
            print(f"Could not move '{filename}': {e}")

    def _create_directory(self, target_dir: str):
        """
        Create a directory if it does not exist.
        
        :param target_dir: The directory path to create.
        """
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)