import os
import subprocess
import shlex

class DJToolMixConverter:
    def run_command(self, command):
        print('Starting conversion...')
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)

        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)

        return result.returncode == 0

    def convert_video(self, img, audio, out):
        ext = os.path.splitext(img)[1].lower()
        is_gif = ext == ".gif"

        if is_gif:
            command = (
                f'ffmpeg -ignore_loop 0 -i "{img}" -i "{audio}" '
                f'-filter_complex "[0:v]scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p[v]" '
                f'-map "[v]" -map 1:a -c:v libx264 -c:a aac -b:a 192k -shortest "{out}"'
            )
        else:
            command = (
                f'ffmpeg -loop 1 -i "{img}" -i "{audio}" '
                f'-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" '
                f'-c:v libx264 -tune stillimage -c:a aac -b:a 192k '
                f'-pix_fmt yuv420p -shortest "{out}"'
            )

        return self.run_command(command)
