<div align="center">

```
  ███╗   ███╗██████╗ ██████╗ ███████╗██╗   ██╗
  ████╗ ████║██╔══██╗╚════██╗██╔════╝╚██╗ ██╔╝
  ██╔████╔██║██████╔╝  ▄███╔╝█████╗   ╚████╔╝ 
  ██║╚██╔╝██║██╔═══╝   ▀▀══╝ ██╔══╝    ╚██╔╝  
  ██║ ╚═╝ ██║██║       ██╗   ██║        ██║   
  ╚═╝     ╚═╝╚═╝       ╚═╝   ╚═╝        ╚═╝   


### 🎧 YouTube → 320 kbps MP3 Downloader with CLI

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-8b5cf6?style=for-the-badge)]()

**Download entire playlists or single tracks from YouTube as high-quality 320 kbps MP3s — with a beautiful terminal UI, user accounts, and automatic artist organization.**

[Features](#-features) · [Installation](#-installation) · [Usage](#-usage) · [Project Structure](#-project-structure) · [Configuration](#-configuration) · [FAQ](#-faq)

---

</div>

## ✨ Features

| Feature | Details |
|---|---|
| 🎵 **320 kbps MP3** | Best-quality audio extraction via FFmpeg |
| 👤 **User Accounts** | Signup, login, logout — passwords are SHA-256 hashed |
| 🔒 **Change Password** | Update credentials safely from within the app |
| 📋 **Batch Download** | Feed a `links.txt` file with as many URLs as you want |
| 🔗 **Single URL** | Paste any YouTube link for a one-off download |
| 📂 **Auto-Organize** | MP3s sorted into `downloads/<Artist>/` folders automatically |
| 🏷️ **ID3 Tags** | Artist, title, and metadata embedded into every file |
| 📜 **Download Logs** | History of every download with status and timestamp |
| 🎨 **Rich CLI UI** | Gorgeous terminal interface built with `rich` + `tqdm` |
| 🐛 **Bug-Fixed** | Duplicate download loop and `NameError` bugs corrected |

---

## 📋 Requirements

- **Python** 3.10 or higher
- **FFmpeg** installed and accessible
- Internet connection

### Installing FFmpeg

<details>
<summary><b>🪟 Windows</b></summary>

1. Download the latest build from [ffmpeg.org/download](https://ffmpeg.org/download.html) or [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
2. Extract the zip and place it somewhere permanent, e.g. `C:\ffmpeg\`
3. The folder structure should look like:
   ```
   C:\ffmpeg\
   └── bin\
       ├── ffmpeg.exe
       ├── ffprobe.exe
       └── ffplay.exe
   ```
4. Open `downloader.py` and set:
   ```python
   "ffmpeg_location": r"C:\ffmpeg\bin",
   ```

</details>

<details>
<summary><b>🐧 Linux (Ubuntu / Debian)</b></summary>

```bash
sudo apt update && sudo apt install ffmpeg -y
```

Then in `downloader.py`, set:
```python
"ffmpeg_location": "",   # empty = use system PATH
```

</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
brew install ffmpeg
```

Then in `downloader.py`, set:
```python
"ffmpeg_location": "",   # empty = use system PATH
```

</details>

---

## 🚀 Installation

### 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mp3fy.git
cd mp3fy
```

### 2 — Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Configure FFmpeg path

Open `downloader.py` and update this line to match your FFmpeg location:

```python
# Windows
"ffmpeg_location": r"C:\ffmpeg\bin",

# Linux / macOS (ffmpeg on PATH)
"ffmpeg_location": "",
```

### 5 — Run the app

```bash
python main.py
```

---

## 🎮 Usage

### First Launch — Create an Account

When you run `mp3fy` for the first time you'll see the welcome screen:

```
┌──────────────────────────────────────────┐
│         ── WELCOME ──                    │
│                                          │
│   [ 1 ]  🔑  Login                       │
│   [ 2 ]  ✨  Sign Up                     │
│   [ 3 ]  ❌  Exit                        │
└──────────────────────────────────────────┘
```

Choose **`2`** to create a new account. Your username must be at least 3 characters and your password at least 6.

---

### Downloading from links.txt (Batch)

This is the fastest way to download many songs at once.

**Step 1 — Add YouTube URLs to `links.txt`**, one per line:

```
https://youtu.be/dQw4w9WgXcQ
https://youtu.be/9bZkp7q19f0
https://youtu.be/JGwWNGJdvx8
```

> Tip: Duplicate URLs (same video ID, different `?si=` tracking token) are handled gracefully — yt-dlp skips already-downloaded files.

**Step 2 — From the main menu, choose `1`:**

```
  Queued 37 track(s) → downloads/

  Downloading  ████████████████░░░░░░  24/37  [00:14<00:08]

  ✔  37 downloaded,  0 failed
  ℹ  Organizing files by artist…
  ✔  Done!  Check your downloads/ folder 🎵
```

---

### Downloading a Single URL

Choose **`2`** from the main menu, then paste any YouTube link:

```
  Paste YouTube URL ❯ https://youtu.be/dQw4w9WgXcQ
```

The track downloads and is organized immediately.

---

### Viewing Download Logs

Choose **`3`** from the main menu to see a table of your full download history:

```
  ┌─────────────────────────────────────────────────────────┐
  │                   Download History                       │
  ├───┬───────────────────────────────┬────────┬────────────┤
  │ # │ Title / URL                   │ Status │ Time       │
  ├───┼───────────────────────────────┼────────┼────────────┤
  │ 1 │ https://youtu.be/dQw4w9WgX…  │ ✔ OK   │ 2025-07-01 │
  │ 2 │ https://youtu.be/9bZkp7q19…  │ ✔ OK   │ 2025-07-01 │
  │ 3 │ https://youtu.be/JGwWNGJdv…  │ ✗ ERR  │ 2025-07-01 │
  └───┴───────────────────────────────┴────────┴────────────┘
```

---

### Changing Your Password

Choose **`4`** from the main menu. You'll be prompted for your current password, then your new password twice for confirmation.

```
  ╔══════════════════════════════╗
  ║      CHANGE PASSWORD         ║
  ╚══════════════════════════════╝

  Current Password: ••••••••
  New Password:     ••••••••
  Confirm:          ••••••••

  ✔  Password changed successfully!
```

---

### Logging Out

Choose **`5`** to log out and return to the welcome screen. Your download logs are preserved.

---

## 📁 Project Structure

```
mp3fy/
│
├── main.py          # App entry point — auth loop + main menu loop
├── auth.py          # Signup / login / change password logic
├── downloader.py    # yt-dlp wrapper — downloads & converts to MP3
├── organizer.py     # Sorts MP3s into downloads/<Artist>/ folders
├── ui.py            # All Rich/tqdm terminal UI components
├── logger.py        # JSON-based download history logger
├── utils.py         # safe_filename(), clean_title() helpers
├── config.py        # Global constants (output dir, quality, file paths)
│
├── links.txt        # Your YouTube URLs — one per line
├── users.json       # Auto-created — stores hashed user accounts
├── logs.json        # Auto-created — stores download history
├── requirements.txt # Python dependencies
│
└── downloads/       # Auto-created — output folder
    ├── Artist Name/
    │   ├── Song Title.mp3
    │   └── Another Song.mp3
    └── Unknown/
        └── Untitled.mp3
```

---

## ⚙️ Configuration

All global settings live in `config.py`:

```python
OUTPUT_DIR = "downloads"   # Where MP3s are saved
QUALITY    = "320"         # Bitrate in kbps (128 / 192 / 256 / 320)
USERS_FILE = "users.json"  # User account store
LOGS_FILE  = "logs.json"   # Download history store
```

To change audio quality, edit `QUALITY`:

```python
QUALITY = "192"   # Lower file size, still good quality
QUALITY = "320"   # Maximum quality (default)
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `yt-dlp` | Downloads audio from YouTube and 1000+ sites |
| `mutagen` | Reads / writes ID3 tags (artist, title) from MP3 files |
| `rich` | Beautiful terminal panels, tables, and text styling |
| `tqdm` | Progress bar for batch downloads |
| `colorama` | Cross-platform ANSI color support on Windows |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🐛 Bugs Fixed vs Original Code

| File | Bug | Fix Applied |
|---|---|---|
| `downloader.py` | Every song downloaded **twice** — `ydl.download()` called two times | Removed duplicate `with yt_dlp.YoutubeDL` block |
| `organizer.py` | `NameError: name 'title' is not defined` in `except` block | Replaced with `os.path.splitext(file)[0]` fallback |
| `organizer.py` | Attempting to rename a file onto itself raised `OSError` | Added `path != new_path` guard before `os.rename` |

---

## ❓ FAQ

<details>
<summary><b>Why does my download fail with "ffmpeg not found"?</b></summary>

You haven't set the `ffmpeg_location` correctly in `downloader.py`. See the [FFmpeg installation](#installing-ffmpeg) section above and point the path to the folder that contains `ffmpeg.exe` (Windows) or the `ffmpeg` binary (Linux/macOS).

</details>

<details>
<summary><b>Can I download entire YouTube playlists?</b></summary>

Yes! Just paste the playlist URL directly into `links.txt` or into the single-URL prompt. yt-dlp will expand the playlist and download every video automatically.

</details>

<details>
<summary><b>What happens if a link is duplicated in links.txt?</b></summary>

yt-dlp detects that the output file already exists and skips it. No duplicate downloads occur.

</details>

<details>
<summary><b>Where are my user credentials stored?</b></summary>

In `users.json` in the project root. Passwords are **never stored in plain text** — they are hashed with SHA-256 before saving.

</details>

<details>
<summary><b>The artist folder is named "Unknown" — how do I fix it?</b></summary>

Some YouTube videos don't embed proper artist metadata. You can manually edit the ID3 tags of the MP3 with a tool like [Mp3tag](https://www.mp3tag.de/en/) and re-run `organize()`, or rename the folders manually.

</details>

<details>
<summary><b>Can I use this on Linux or macOS?</b></summary>

Yes. Set `"ffmpeg_location": ""` in `downloader.py` so yt-dlp uses your system FFmpeg. Everything else works cross-platform.

</details>

---

## 📄 License

This project is released under the [MIT License](LICENSE). You are free to use, modify, and distribute it for personal or educational purposes.

---

<div align="center">

Made with ❤️ and Python &nbsp;·&nbsp; Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) + [FFmpeg](https://ffmpeg.org)

**If this project helped you, consider giving it a ⭐ on GitHub!**

</div>
