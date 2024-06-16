import os
import re
import threading

class DJToolRegexHelper:
    def __init__(self) -> None:
        self.dir = None
        self.thread_completion_event = threading.Event()

    def remove_sqr_brackets(self) -> None:
        # Regular expression to match text within brackets, including the brackets
        pattern = re.compile(r"\[[^\]]*\]", re.IGNORECASE)
        self._remove(self.dir, pattern)

    def remove_redundant_mp3(self) -> None:
        pattern = re.compile(r'(\.mp3)+$')
        self._remove(self.dir, pattern, replace_with='.mp3')

    def _remove(self, dir: str, pattern: re.Pattern, replace_with: str = '') -> None:
        # Iterate over the files in the specified dir
        for filename in os.listdir(dir):
            # Check if the file is an mp3 file
            if filename.endswith('.mp3'):
                # Apply the pattern to the filename
                new_filename = re.sub(pattern, replace_with, filename).strip()
                # Construct the full old and new paths
                old_file = os.path.join(dir, filename)
                new_file = os.path.join(dir, new_filename)
                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {filename} -> {new_filename}')
        
        self.thread_completion_event.set()