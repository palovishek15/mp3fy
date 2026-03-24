import re


def safe_filename(name: str) -> str:
    """Remove characters invalid on Windows/Linux filesystems."""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = name.strip(". ")          # no leading/trailing dots or spaces
    return name or "Unknown"


def clean_title(title: str) -> str:
    """Strip clutter words and brackets from YouTube video titles."""
    title = re.sub(r'\(.*?\)|\[.*?\]', '', title)
    title = re.sub(r'(?i)(lyric(s|al)?|official|video|audio|hd|hq|4k|song|music)', '', title)
    title = title.replace('|', '-')
    return " ".join(title.split()).strip()
