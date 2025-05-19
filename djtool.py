import tkinter as tk
from djtool_gui import DJToolGUI
from djtool_downloader import DJToolDownloader
from djtool_regex import DJToolRegexHelper
from djtool_albumchanger import DJToolAlbumChanger
from djtool_mixconverter import DJToolMixConverter

class DJTool:
    def __init__(self):
        self.downloader = None
        self.albumchanger = None
        self.regex = None
        self.mixconverter = None

if __name__ == "__main__":
    root = tk.Tk()
    tool = DJTool()
    tool.downloader = DJToolDownloader()
    tool.albumchanger = DJToolAlbumChanger()
    tool.regex = DJToolRegexHelper()
    tool.mixconverter = DJToolMixConverter()
    tool_gui = DJToolGUI(tool, root)
    root.mainloop()