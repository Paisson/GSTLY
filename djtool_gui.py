from tkinter import ttk
from djtool_downloader_gui import DJToolDownloaderGUI
from djtool_regex_gui import DJToolRegexHelperGUI
from djtool_albumchanger_gui import DJToolAlbumChangerGUI
from djtool_mixconverter_gui import DJToolMixConverterGUI

class DJToolGUI:
    def __init__(self, tool, root):
        self.root = root
        self.tool = tool
        self.root.title("DJ Tool")

        # Create a notebook
        self.notebook = ttk.Notebook(root)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)

        # Add the notebook to the root
        self.notebook.pack(expand=1, fill="both")
        
        # Create an instance of DJToolDownloaderGUI within the first tab
        self.downloader_gui = DJToolDownloaderGUI(self.tool.downloader, self.tab1)
        self.album_gui = DJToolAlbumChangerGUI(self.tool.albumchanger, self.tab2)
        self.regex_gui = DJToolRegexHelperGUI(self.tool.regex, self.tab3)
        self.converter_gui = DJToolMixConverterGUI(self.tool.mixconverter, self.tab4)

        # Add tabs to the notebook
        self.notebook.add(self.tab1, text="Downloader")
        self.notebook.add(self.tab2, text="Album Changer")
        self.notebook.add(self.tab3, text="Regex Helper")
        self.notebook.add(self.tab4, text="Mix Converter")
