from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
import pyfiglet

console = Console()

def show_banner():
    banner = pyfiglet.figlet_format("Study Planner", font="slant")
    console.print(f"[bold cyan]{banner}[/bold cyan]")

def show_menu():
    console.print(Panel(
        "[1] Add Subject\n[2] Mark Progress\n[3] View Schedule\n"
        "[4] View Progress\n[5] Save & Exit",
        title="Menu", border_style="magenta"
    ))

def show_subjects_table(subjects):
    table = Table(title="Your Subjects")
    table.add_column("Name", style="cyan")
    table.add_column("Deadline", style="yellow")
    table.add_column("Days Left", style="red")
    table.add_column("Progress", style="green")

    for s in subjects:
        # TODO: color-code days_left based on urgency
        table.add_row(
            s.name,
            str(s.deadline),
            str(s.days_left),
            f"{s.progress_percent}%"
        )
    console.print(table)

def show_schedule(schedule: dict):
    # TODO: display today's allocated hours per subject nicely
    # e.g. using a Panel or Table, color-coded by urgency
    pass