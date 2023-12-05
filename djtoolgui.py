from tkinter import filedialog, simpledialog, ttk
import tkinter as tk


class DJToolGUI:
    def __init__(self, tool, root):
        self.tool = tool
        self.root = root

        self.root.title("DJ Tool")

        # Create a notebook
        self.notebook = ttk.Notebook(root)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Downloader")
        self.notebook.add(self.tab2, text="Converter")
        self.notebook.add(self.tab3, text="Labeler")

        self.notebook.pack(expand=1, fill="both")

        # Create "Link" label and entry
        self.link_label = tk.Label(self.tab1, text="Link")
        self.link_entry = tk.Entry(self.tab1, width=40)

        # Create "Paste Tracklists" label and text entry
        self.track_label = tk.Label(self.tab1, text="Tracklist\nor\nLinklist")
        self.text_entry = tk.Text(self.tab1, height=5, width=40)

        # Create Checkbox for playlist download
        self.playlist_checkbox = tk.Checkbutton(self.tab1, text="Allow Playlist", variable=self.tool.allow_playlist)

        # Create Buttons
        self.browse_button = tk.Button(self.tab1, text="Path", command=self.set_download_path)
        self.submit_button = tk.Button(self.tab1, text="Start", command=self.submit)
        self.max_downloads_button = tk.Button(self.tab1, text=f'Max: {self.tool.max_downloads}', command=self.set_max_downloads)

        # Pack the widgets in the new order
        self.link_label.grid(row=0, column=0, pady=10, sticky=tk.E)
        self.link_entry.grid(row=0, column=1, pady=10, padx=5,sticky=tk.W)
        self.browse_button.grid(row=0, column=2, pady=10, padx=5, sticky=tk.W)

        self.track_label.grid(row=1, column=0, pady=10, sticky=tk.E)
        self.text_entry.grid(row=1, column=1, pady=10, padx=5)

        self.max_downloads_button.grid(row=2, column=0, pady=10, padx=5, sticky=tk.E)
        self.playlist_checkbox.grid(row=2, column=1, pady=10, padx=5)
        self.submit_button.grid(row=2, column=2, pady=10, padx=5, sticky=tk.E)


    def set_max_downloads(self):
        self.tool.max_downloads = simpledialog.askinteger('Set max Songs', prompt='Enter the maximum number of songs to download:')
        self.max_downloads_button["text"] = f'Max: {self.tool.max_downloads}'
        print(f'Max downloads set to {self.tool.max_downloads}')

    def set_download_path(self):
        self.tool.download_path = filedialog.askdirectory()
        print(f'Path set to {self.tool.download_path}')

    def submit(self):
        # Accessing the values entered in the fields
        search_query = self.text_entry.get("1.0", tk.END)
        link = self.link_entry.get()

        self.tool.download_video(search_query) if search_query != '\n' else None
        self.tool.download_video(link) if link != '\n' else None
