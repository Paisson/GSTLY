from tkinter import filedialog
import tkinter as tk

class DJToolConverterGUI:
    def __init__(self, converter, root):

        self.converter = converter
        self.root = root

        # Configure column weights
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)  # Button column with higher weight
        root.columnconfigure(2, weight=1)

        # Configure row weights
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=2)  # Button row with higher weight
        root.rowconfigure(2, weight=1)

        self.select_folder_button = tk.Button(root, text="MP3 Converter", command=self.select_input_folder)
        self.select_folder_button.grid(row=1, column=1)

        # Create Info Label
        self.info_label = tk.Label(self.root, text='')

    def select_input_folder(self):
        path = filedialog.askdirectory(title='Select Directory')
        if path:
            self.converter.convert_wav_to_mp3(path)
            self.info_label.grid(row=2, column=1, pady=10)
            self.info_label['text'] = 'Working'
            self.root.after(100, self.check_thread_completion)

    def check_thread_completion(self):
        if self.converter.thread_completion_event.is_set():
            self.info_label['text'] = 'Finished'
            self.converter.thread_completion_event.clear()

        else:
            self.root.after(100, self.check_thread_completion)
        