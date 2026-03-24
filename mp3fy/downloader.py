import yt_dlp
import os
from config import OUTPUT_DIR, QUALITY

os.makedirs(OUTPUT_DIR, exist_ok=True)


def download_song(url: str) -> dict:
    """
    Download a YouTube URL as 320 kbps MP3.
    Returns a dict: {"title": ..., "status": "ok" | "error", "error": ...}
    """
    result = {"url": url, "title": "", "status": "ok", "error": ""}

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",

        # ── Change this to wherever ffmpeg is installed on your machine ──
        # Windows example:  r"C:\ffmpeg\bin"
        # Linux/Mac:        leave as empty string "" (ffmpeg on PATH)
        "ffmpeg_location": r"C:\ffmpeg\bin",

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": QUALITY,
            },
            {
                "key": "FFmpegMetadata",   # embeds artist/title tags
            },
        ],

        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            result["title"] = info.get("title", url) if info else url
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    return result
