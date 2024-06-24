import tkinter as tk
from djtoolgui import DJToolGUI
from djtooldownloader import DJToolDownloader
# from djtoolconverter import DJToolConverter
from djtoolregex import DJToolRegexHelper
from djtoolalbumchanger import DJToolAlbumChanger

class DJTool:
    def __init__(self):
        self.downloader = None
        # self.converter = None
        self.albumchanger = None
        self.regex = None

if __name__ == "__main__":
    root = tk.Tk()
    tool = DJTool()
    tool.downloader = DJToolDownloader()
    #tool.converter = DJToolConverter()
    tool.albumchanger = DJToolAlbumChanger()
    tool.regex = DJToolRegexHelper()
    tool_gui = DJToolGUI(tool, root)
    root.mainloop()