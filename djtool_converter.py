import os
import subprocess
import threading

class DJToolConverter:
    def __init__(self):
        self.path = None
        self.thread_completion_event = threading.Event()

    def convert_wav_to_mp3(self, path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".wav"):
                    path = os.path.join(root, file)
                    path = os.path.splitext(file)[0] + ".mp3"
                    path = os.path.join(path, path)

                    subprocess.run([
                        "ffmpeg",
                        "-i", path,
                        "-vn",  # No video
                        "-ar", "44100",  # Audio sample rate
                        "-ac", "2",      # Stereo
                        "-b:a", "192k",  # Audio bitrate
                        path
                    ])

                    # Delete the original .wav file after conversion
                    os.remove(path)
                if file.endswith(".png"):
                    path = os.path.join(root, file)
                    os.remove(path)
                if file.endswith(".jpg"):
                    path = os.path.join(root, file)
                    os.remove(path)

            self.thread_completion_event.set()
