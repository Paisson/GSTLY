import subprocess
import threading
import tkinter as tk


class DJToolDownloader:
    def __init__(self):
        self.download_path = r'C:\Users\Shark\Music\Music\new'
        self.max_downloads = 0
        self.allow_playlist = tk.BooleanVar()
        self.allow_playlist.set(False)
        self.p = None

        self.thread_completion_event = threading.Event()
        self.thread_cancel_event = threading.Event()

    def run_command(self, command):
        self.p = subprocess.Popen(command)


    def download_video(self, search_query):
        allow_playlist = "--no-playlist" if not self.allow_playlist.get() else ""
        max_downloads_option = f"--max-downloads {self.max_downloads}" if self.max_downloads > 0 else ""

        command = (
            f'yt-dlp -P {self.download_path} '
            f'{allow_playlist} --add-metadata --embed-thumbnail --match-filter "duration < 1800" '
            f'{max_downloads_option} --extract-audio --audio-format mp3 {search_query}'
            )


        self.run_command(command)
        self.p.wait()
        self.thread_completion_event.set()

    def cancel_download(self):
        self.p.kill()
        self.thread_cancel_event.set()



