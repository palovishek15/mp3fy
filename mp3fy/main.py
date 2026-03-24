"""
mp3fy  ─  YouTube → 320 kbps MP3 Downloader
Run:  python main.py
"""

from rich.prompt import Prompt
from rich.align import Align
from tqdm import tqdm

import ui
import auth
import logger
from downloader import download_song
from organizer import organize
from config import OUTPUT_DIR


# ──────────────────────────────────────────────
#  Download helpers
# ──────────────────────────────────────────────

def _run_downloads(urls: list[str]):
    ui.print_separator()
    ui.print_info(f"Queued {len(urls)} track(s)  →  {OUTPUT_DIR}/")
    ui.console.print()

    ok = err = 0
    for url in tqdm(urls, desc="  Downloading", unit="track",
                    bar_format="  {l_bar}{bar:30}{r_bar}",
                    colour="cyan"):
        result = download_song(url)
        if result["status"] == "ok":
            ok += 1
        else:
            err += 1
            ui.print_error(f"Failed: {url[:60]}")
            ui.console.print(f"         [dim]{result['error'][:80]}[/dim]")
        logger.log_download(url, result["status"], result.get("title", ""))

    ui.print_separator()
    ui.print_success(f"{ok} downloaded,  {err} failed")
    ui.print_info("Organizing files by artist…")
    organize()
    ui.print_success("Done!  Check your downloads/ folder 🎵")
    ui.console.print()
    ui.console.input(" [bold dim]Press Enter to continue…[/bold dim] ")


def download_from_file():
    try:
        with open("links.txt", "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        ui.print_error("links.txt not found in the current directory.")
        ui.console.input(" [bold dim]Press Enter to go back…[/bold dim] ")
        return

    if not urls:
        ui.print_error("links.txt is empty.")
        ui.console.input(" [bold dim]Press Enter to go back…[/bold dim] ")
        return

    _run_downloads(urls)


def download_single():
    ui.console.print()
    url = Prompt.ask("[bold yellow]  Paste YouTube URL[/bold yellow]").strip()
    if not url:
        return
    _run_downloads([url])


# ──────────────────────────────────────────────
#  Auth flow
# ──────────────────────────────────────────────

def auth_loop() -> str | None:
    """Returns logged-in username, or None to exit."""
    while True:
        ui.show_logo()
        choice = ui.show_auth_menu()

        if choice == "1":
            user = auth.login()
            if user:
                return user

        elif choice == "2":
            user = auth.signup()
            if user:
                return user

        elif choice == "3":
            ui.animate_exit()
            return None

        else:
            ui.print_error("Invalid choice.")
            import time; time.sleep(0.8)


# ──────────────────────────────────────────────
#  Main loop
# ──────────────────────────────────────────────

def main_loop(username: str) -> bool:
    """Returns True to restart auth, False to exit."""
    while True:
        ui.show_dashboard(username)
        choice = ui.show_main_menu()

        if choice == "1":
            download_from_file()

        elif choice == "2":
            download_single()

        elif choice == "3":
            ui.show_logs(logger.get_logs())

        elif choice == "4":
            ui.console.print()
            auth.change_password(username)
            ui.console.input(" [bold dim]Press Enter to continue…[/bold dim] ")

        elif choice == "5":
            ui.print_info(f"Logged out. See you, [cyan]{username}[/cyan]!")
            import time; time.sleep(1)
            return True   # back to auth screen

        elif choice == "6":
            ui.animate_exit()
            return False

        else:
            ui.print_error("Invalid choice.")
            import time; time.sleep(0.8)


# ──────────────────────────────────────────────
#  Entry point
# ──────────────────────────────────────────────

def main():
    while True:
        username = auth_loop()
        if username is None:
            break
        restart = main_loop(username)
        if not restart:
            break


if __name__ == "__main__":
    main()
