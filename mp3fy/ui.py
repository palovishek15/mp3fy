from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.rule import Rule
from rich import box
import time

console = Console()


BANNER = r"""
  ███╗   ███╗██████╗ ██████╗ ███████╗██╗   ██╗
  ████╗ ████║██╔══██╗╚════██╗██╔════╝╚██╗ ██╔╝
  ██╔████╔██║██████╔╝  ▄███╔╝█████╗   ╚████╔╝ 
  ██║╚██╔╝██║██╔═══╝   ▀▀══╝ ██╔══╝    ╚██╔╝  
  ██║ ╚═╝ ██║██║       ██╗   ██║        ██║   
  ╚═╝     ╚═╝╚═╝       ╚═╝   ╚═╝        ╚═╝   
"""

TAGLINE = "🎧  YouTube → 320kbps MP3  |  Fast • Clean • Organized"


def clear():
    console.clear()


def show_logo():
    clear()
    logo = Text(BANNER, style="bold cyan")
    tagline = Text(f"\n{TAGLINE}\n", style="italic dim white", justify="center")
    combined = Text.assemble(logo, tagline)
    console.print(Panel(
        Align.center(combined),
        border_style="bright_magenta",
        box=box.DOUBLE_EDGE,
        padding=(0, 4),
    ))


def show_auth_menu() -> str:
    console.print()
    table = Table(
        show_header=False,
        box=box.SIMPLE_HEAD,
        border_style="dim white",
        padding=(0, 3),
    )
    table.add_column(justify="center", style="bold white", min_width=32)

    table.add_row("[bold cyan][ 1 ][/bold cyan]  🔑  Login")
    table.add_row("[bold cyan][ 2 ][/bold cyan]  ✨  Sign Up")
    table.add_row("[bold cyan][ 3 ][/bold cyan]  ❌  Exit")

    console.print(Align.center(
        Panel(table, title="[bold magenta]── WELCOME ──[/bold magenta]",
              border_style="magenta", box=box.ROUNDED, padding=(1, 6))
    ))
    console.print()
    return console.input("[bold bright_green] ❯  Choice: [/bold bright_green]").strip()


def show_dashboard(username: str):
    clear()
    show_logo()
    console.print()

    info = Table(show_header=False, box=None, padding=(0, 2))
    info.add_column(style="dim cyan", min_width=12)
    info.add_column(style="bold white")

    info.add_row("👤  User", f"[bold green]{username}[/bold green]")
    info.add_row("🎯  Quality", "[bold yellow]320 kbps MP3[/bold yellow]")
    info.add_row("📁  Output", "[bold cyan]downloads/[/bold cyan]")
    info.add_row("⚡  Mode", "[bold magenta]Auto-Organize by Artist[/bold magenta]")

    console.print(Align.center(
        Panel(info, title="[bold white]── SESSION ──[/bold white]",
              border_style="bright_blue", box=box.ROUNDED, padding=(1, 4))
    ))


def show_main_menu() -> str:
    console.print()
    table = Table(
        show_header=False,
        box=box.SIMPLE_HEAD,
        border_style="dim white",
        padding=(0, 3),
    )
    table.add_column(justify="left", style="bold white", min_width=36)

    table.add_row("[bold green][ 1 ][/bold green]  🎵  Download from links.txt")
    table.add_row("[bold green][ 2 ][/bold green]  🔗  Download a single URL")
    table.add_row("[bold green][ 3 ][/bold green]  📜  View Download Logs")
    table.add_row("[bold yellow][ 4 ][/bold yellow]  🔒  Change Password")
    table.add_row("[bold red][ 5 ][/bold red]  🚪  Logout")
    table.add_row("[bold red][ 6 ][/bold red]  ❌  Exit")

    console.print(Align.center(
        Panel(table, title="[bold cyan]── MAIN MENU ──[/bold cyan]",
              border_style="cyan", box=box.ROUNDED, padding=(1, 6))
    ))
    console.print()
    return console.input("[bold bright_green] ❯  Choice: [/bold bright_green]").strip()


def show_logs(logs: list):
    clear()
    show_logo()

    if not logs:
        console.print(Align.center(
            Panel("[dim]No downloads recorded yet.[/dim]",
                  title="[bold]── LOGS ──[/bold]",
                  border_style="yellow", box=box.ROUNDED, padding=(1, 4))
        ))
        console.input("\n [bold dim]Press Enter to go back...[/bold dim] ")
        return

    table = Table(
        title="[bold white]Download History[/bold white]",
        box=box.SIMPLE_HEAD,
        border_style="bright_blue",
        header_style="bold cyan",
        show_lines=False,
        padding=(0, 2),
    )
    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("Title / URL", style="white", max_width=50)
    table.add_column("Status", justify="center", width=10)
    table.add_column("Time", style="dim", width=20)

    for i, entry in enumerate(logs[-30:], 1):
        status_icon = "[bold green]✔ OK[/bold green]" if entry.get("status") == "ok" else "[bold red]✗ ERR[/bold red]"
        table.add_row(
            str(i),
            entry.get("url", "")[:60],
            status_icon,
            entry.get("time", ""),
        )

    console.print()
    console.print(Align.center(table))
    console.print()
    console.input(" [bold dim]Press Enter to go back...[/bold dim] ")


def print_separator():
    console.print(Rule(style="dim bright_blue"))


def print_success(msg: str):
    console.print(f"\n[bold bright_green]  ✔  {msg}[/bold bright_green]")


def print_error(msg: str):
    console.print(f"\n[bold red]  ✗  {msg}[/bold red]")


def print_info(msg: str):
    console.print(f"\n[bold cyan]  ℹ  {msg}[/bold cyan]")


def animate_exit():
    console.print()
    goodbye = Text("  Goodbye! Enjoy your music  🎵  ", style="bold bright_cyan")
    console.print(Align.center(Panel(goodbye, border_style="cyan",
                                     box=box.DOUBLE, padding=(1, 6))))
    time.sleep(1)
