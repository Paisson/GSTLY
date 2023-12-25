from tkinter import filedialog, simpledialog
import tkinter as tk
import threading

class DJToolDownloaderGUI:
    def __init__(self, downloader, root):

        self.root = root
        self.downloader = downloader
        
        # Create "Link" label and entry
        self.link_label = tk.Label(self.root, text="Link")
        self.link_entry = tk.Entry(self.root, width=60)


        # Create Checkbox for playlist download
        self.playlist_checkbox = tk.Checkbutton(self.root, text="Allow Playlist", variable=self.downloader.allow_playlist)

        # Create Buttons
        self.browse_button = tk.Button(self.root, text="Path", command=self.set_download_path)
        self.submit_button = tk.Button(self.root, text="Start", command=self.submit)
        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel_download)
        self.max_downloads_button = tk.Button(self.root, text=f'Max: {self.downloader.max_downloads}', command=self.set_max_downloads)

        # Create Info Label
        self.info_label = tk.Label(self.root, text='')

        # Pack the widgets in the new order
        self.link_label.grid(row=0, column=0, pady=10, sticky=tk.E)
        self.link_entry.grid(row=0, column=1, pady=10, padx=5, sticky=tk.W)
        self.browse_button.grid(row=0, column=2, pady=10, padx=5, sticky=tk.W)

        self.max_downloads_button.grid(row=2, column=0, pady=10, padx=5, sticky=tk.E)
        self.playlist_checkbox.grid(row=2, column=1, pady=10, padx=5)
        self.submit_button.grid(row=2, column=2, pady=10, padx=5, sticky=tk.E)
        

    def set_max_downloads(self):
        self.downloader.max_downloads = simpledialog.askinteger('Set max Songs', prompt='Enter the maximum number of songs to download:')
        self.max_downloads_button["text"] = f'Max: {self.downloader.max_downloads}'
        print(f'Max downloads set to {self.downloader.max_downloads}')

    def set_download_path(self):
        self.downloader.download_path = filedialog.askdirectory()
        print(f'Path set to {self.downloader.download_path}')


    def download_worker(self, query):
        self.submit_button.grid_forget() 
        self.cancel_button.grid(row=2, column=2, pady=10, padx=5, sticky=tk.E)
        self.downloader.download_video(query)

    def check_thread_completion(self):
        if self.downloader.thread_cancel_event.is_set() or self.downloader.thread_completion_event.is_set():
            self.cancel_button.grid_forget()
            self.submit_button.grid(row=2, column=2, pady=10, padx=5, sticky=tk.E)


        if self.downloader.thread_completion_event.is_set() and self.downloader.thread_cancel_event.is_set():
            self.info_label['text'] = 'Canceled'
            self.downloader.thread_completion_event.clear()
            self.downloader.thread_cancel_event.clear()

        if self.downloader.thread_completion_event.is_set():
            self.info_label['text'] = 'Finished'
            self.downloader.thread_completion_event.clear()
            
        else:
            self.root.after(100, self.check_thread_completion)


    def submit(self):
        link = self.link_entry.get()

        self.info_label.grid(row=3, column=1, pady=10)
        self.info_label['text'] = 'Working'

        if link != '\n':
            thread = threading.Thread(target=self.download_worker, args=(link,))
            thread.start()

        self.root.after(100, self.check_thread_completion)

    def cancel_download(self):
        # Set the event to signal cancellation
        self.cancel_button.grid_forget()
        self.submit_button.grid(row=2, column=2, pady=10, padx=5, sticky=tk.E)
        self.downloader.cancel_download()

            



