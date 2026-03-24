import os
from mutagen.easyid3 import EasyID3
from utils import safe_filename
from config import OUTPUT_DIR


def organize():
    """
    Move every MP3 in downloads/ into a sub-folder named after its artist tag.
    Falls back to 'Unknown' if the tag is missing.
    """
    if not os.path.isdir(OUTPUT_DIR):
        return

    for file in os.listdir(OUTPUT_DIR):
        if not file.endswith(".mp3"):
            continue

        path = os.path.join(OUTPUT_DIR, file)

        try:
            audio = EasyID3(path)
            artist = audio.get("artist", ["Unknown"])[0]
            title  = audio.get("title",  [os.path.splitext(file)[0]])[0]
        except Exception:
            artist = "Unknown"
            title  = os.path.splitext(file)[0]   # ← was a NameError in original

        artist = safe_filename(artist)[:80]
        title  = safe_filename(title)[:100]

        artist_folder = os.path.join(OUTPUT_DIR, artist)
        os.makedirs(artist_folder, exist_ok=True)

        new_path = os.path.join(artist_folder, f"{title}.mp3")

        if path != new_path and not os.path.exists(new_path):
            os.rename(path, new_path)
