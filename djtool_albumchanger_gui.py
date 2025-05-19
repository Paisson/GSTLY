from tkinter import filedialog
import tkinter as tk

class DJToolAlbumChangerGUI:
    def __init__(self, albumchanger, root):
        self.albumchanger = albumchanger
        self.root = root
        
     # Configure column weights
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)  # Button column with higher weight
        root.columnconfigure(2, weight=1)

        # Configure row weights
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=2)  # Button row with higher weight
        root.rowconfigure(2, weight=1)

        self.select_folder_button = tk.Button(root, text="Album Changer", command=self.select_input_folder)
        self.select_folder_button.grid(row=1, column=1)

    def select_input_folder(self):
        self.albumchanger.dir = filedialog.askdirectory(title='Select Directory')
        if self.albumchanger.dir:
            self.albumchanger.set_album_tags()