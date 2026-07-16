from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner() -> None:
    """Display NAS Sentinel startup banner."""

    console.print(
        Panel.fit(
            "[bold cyan]NAS Sentinel[/bold cyan]\n"
            "[green]Version 1.0[/green]\n"
            "Personal NAS Monitoring System",
            title="🚀 Starting",
            border_style="blue",
        )
    )
