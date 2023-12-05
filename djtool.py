from DJToolGUI import DJToolGUI
import tkinter as tk
import subprocess


class DJTool:
    def __init__(self):
        self.download_path = r'C:\Users\Shark\Music\Music\new'
        self.max_downloads = 0
        self.allow_playlist = tk.BooleanVar()
        self.allow_playlist.set(False)

    # Runs the command and prints result
    def run_command(self, command):
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)

    # Start download with max_downloads
    def download_video(self, search_query):
        if self.allow_playlist.get() is False:
            if self.max_downloads > 0: 
                command = f'yt-dlp -P {self.download_path} --no-playlist --add-metadata --embed-thumbnail --match-filter "duration < 1800" --max-downloads {self.max_downloads} {search_query}'
            else:
                command = f'yt-dlp -P {self.download_path} --no-playlist --add-metadata --embed-thumbnail --match-filter "duration < 1800" {search_query}'
        else: 
            if self.max_downloads > 0: 
                command = f'yt-dlp -P {self.download_path} --add-metadata --embed-thumbnail --match-filter "duration < 1800" --max-downloads {self.max_downloads} {search_query}'
            else:
                command = f'yt-dlp -P {self.download_path} --add-metadata --embed-thumbnail --match-filter "duration < 1800" {search_query}'
        self.run_command(command)   
        print('Done') 


if __name__ == "__main__":
    root = tk.Tk()
    tool = DJTool()
    gui = DJToolGUI(tool, root)
    root.mainloop()
