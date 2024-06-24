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

    # def remove_redundant_mp3(self) -> None:
    #    pattern = re.compile(r'(\.mp3)+$')
    #    self._remove(self.dir, pattern, replace_with='.mp3')

    def remove_free_dl(self):
        pattern = re.compile(r'FREE DL', re.IGNORECASE)
        self._remove(self.dir, pattern)
        pattern = re.compile(r'Premiere', re.IGNORECASE)
        self._remove(self.dir, pattern)

    def _remove(self, dir: str, pattern: re.Pattern, replace_with: str = '') -> None:
        for root, dirs, files in os.walk(dir):
            # Iterate over the files in the directory
            for filename in files:
                # Check if the file is an mp3 file
                if filename.endswith('.mp3'):
                    # Apply the pattern to the filename
                    new_filename = re.sub(pattern, replace_with, filename).strip()
                    if new_filename != filename:  # Check if the filename has changed
                        # Construct the full old and new paths
                        old_file = os.path.join(root, filename)
                        new_file = os.path.join(root, new_filename)
                        # Rename the file
                        if not os.path.exists(new_file):
                            os.rename(old_file, new_file)
                        print(f'Renamed: {old_file} -> {new_file}')
        
        self.thread_completion_event.set()
        