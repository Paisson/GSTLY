import os
import eyed3

class DJToolAlbumChanger:
    def __init__(self) -> None:
        self.dir = None

    def set_album_tags(self):
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                if file.endswith(".mp3"):
                    mp3_path = os.path.join(root, file)
                    dir_name = os.path.basename(root)

                    audiofile = eyed3.load(mp3_path)
                    if audiofile is None:
                        print(f"Could not load {mp3_path}, skipping...")
                        continue

                    if audiofile.tag is None:
                        audiofile.initTag()
                    
                    audiofile.tag.album = dir_name
                    audiofile.tag.save()
                    print('Album Tag Set')
            print('Finished')