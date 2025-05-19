import os
import re
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

class DJToolMixConverterGUI:
    def __init__(self, converter, root):
        self.root = root
        self.converter = converter

        self.mp3_file = None
        self.image_file = None
        self.conversion_thread = None

        self.create_widgets()

    def create_widgets(self):
        self.mp3_button = tk.Button(self.root, text="Select MP3 File", command=self.select_mp3_file)
        self.mp3_button.grid(row=0, column=0, padx=10, pady=10)

        self.image_button = tk.Button(self.root, text="Select Image File", command=self.select_image_file)
        self.image_button.grid(row=0, column=1, padx=10, pady=10)

        self.status_label = tk.Label(self.root, text="Status: Idle")
        self.status_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.convert_button = tk.Button(self.root, text="Start Conversion", command=self.toggle_conversion)
        self.convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def update_status_safe(self, message):
        self.root.after(0, lambda: self.status_label.config(text=f"Status: {message}"))

    def show_message_safe(self, title, msg, error=False):
        self.root.after(0, lambda: (
            messagebox.showerror(title, msg) if error else messagebox.showinfo(title, msg)
        ))

    def select_mp3_file(self):
        self.mp3_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.mp3_file:
            print(f"Selected MP3 file: {self.mp3_file}")

    def select_image_file(self):
        self.image_file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_file:
            print(f"Selected Image file: {self.image_file}")

    def start_conversion(self):
        self.update_status_safe("Converting...")

        if not self.mp3_file or not self.image_file:
            self.show_message_safe("Missing Files", "Please select both an MP3 and an Image file.", error=True)
            self.update_status_safe("Idle")
            return

        filename_without_extension = re.sub(r'\.mp3$', '', os.path.basename(self.mp3_file))
        output_file_path = os.path.join("C:/Users/Shark/Music/mixed/mp4", f"{filename_without_extension}.mp4")

        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)  # Ensure output directory exists

        success = self.converter.convert_video(self.image_file, self.mp3_file, output_file_path)

        if success:
            self.show_message_safe("Success", f"Conversion completed successfully.\nSaved to:\n{output_file_path}")
            self.update_status_safe("Done")
        else:
            self.show_message_safe("Failed", "Conversion failed.", error=True)
            self.update_status_safe("Failed")

    def toggle_conversion(self):
        if self.conversion_thread and self.conversion_thread.is_alive():
            self.show_message_safe("In Progress", "A conversion is already running. Please wait...")
        else:
            self.conversion_thread = threading.Thread(target=self.start_conversion)
            self.conversion_thread.start()