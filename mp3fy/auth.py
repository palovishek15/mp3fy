import json
import os
import hashlib
import getpass
from config import USERS_FILE
from ui import console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import box


# ──────────────────────────────────────────────
#  Helpers
# ──────────────────────────────────────────────

def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def _save_users(users: dict):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def _get_password(prompt_text: str) -> str:
    """Cross-platform secure password input."""
    try:
        return getpass.getpass(prompt_text)
    except Exception:
        return Prompt.ask(prompt_text, password=True)


# ──────────────────────────────────────────────
#  Auth Functions
# ──────────────────────────────────────────────

def signup() -> str | None:
    console.print(Panel(
        "[bold cyan]  CREATE NEW ACCOUNT  [/bold cyan]",
        border_style="cyan", box=box.DOUBLE
    ))

    username = Prompt.ask("[bold yellow]  Username[/bold yellow]").strip()

    users = _load_users()
    if username in users:
        console.print("[bold red]  ✗  Username already taken.[/bold red]\n")
        return None

    if len(username) < 3:
        console.print("[bold red]  ✗  Username must be at least 3 characters.[/bold red]\n")
        return None

    password = _get_password("  Password: ")
    if len(password) < 6:
        console.print("[bold red]  ✗  Password must be at least 6 characters.[/bold red]\n")
        return None

    confirm = _get_password("  Confirm Password: ")
    if password != confirm:
        console.print("[bold red]  ✗  Passwords do not match.[/bold red]\n")
        return None

    users[username] = {"password": _hash(password)}
    _save_users(users)

    console.print(f"\n[bold green]  ✔  Account created! Welcome, [cyan]{username}[/cyan] 🎉[/bold green]\n")
    return username


def login() -> str | None:
    console.print(Panel(
        "[bold magenta]  LOGIN TO MP3FY  [/bold magenta]",
        border_style="magenta", box=box.DOUBLE
    ))

    username = Prompt.ask("[bold yellow]  Username[/bold yellow]").strip()
    password = _get_password("  Password: ")

    users = _load_users()

    if username not in users or users[username]["password"] != _hash(password):
        console.print("[bold red]  ✗  Invalid username or password.[/bold red]\n")
        return None

    console.print(f"\n[bold green]  ✔  Welcome back, [cyan]{username}[/cyan]! 🎧[/bold green]\n")
    return username


def change_password(username: str) -> bool:
    console.print(Panel(
        "[bold yellow]  CHANGE PASSWORD  [/bold yellow]",
        border_style="yellow", box=box.DOUBLE
    ))

    users = _load_users()

    old = _get_password("  Current Password: ")
    if users[username]["password"] != _hash(old):
        console.print("[bold red]  ✗  Current password is incorrect.[/bold red]\n")
        return False

    new = _get_password("  New Password: ")
    if len(new) < 6:
        console.print("[bold red]  ✗  Password must be at least 6 characters.[/bold red]\n")
        return False

    confirm = _get_password("  Confirm New Password: ")
    if new != confirm:
        console.print("[bold red]  ✗  Passwords do not match.[/bold red]\n")
        return False

    users[username]["password"] = _hash(new)
    _save_users(users)

    console.print("[bold green]  ✔  Password changed successfully![/bold green]\n")
    return True
