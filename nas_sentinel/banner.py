from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_banner() -> None:
    """Display NAS Sentinel startup banner."""

    table = Table.grid(padding=(0, 2))

    table.add_row("[bold cyan]Application[/]", "NAS Sentinel")
    table.add_row("[bold green]Version[/]", "1.0")
    table.add_row("[bold yellow]Platform[/]", "Linux Mint")
    table.add_row("[bold magenta]Automation[/]", "systemd Timer")
    table.add_row("[bold blue]Storage[/]", "Nextcloud WebDAV")
    table.add_row("[bold white]Notifications[/]", "ntfy.sh")
    table.add_row("[bold red]Logging[/]", "Rich + Rotating Logs")

    console.print(
        Panel(
            table,
            title="[bold cyan]🚀 NAS Sentinel Starting[/]",
            subtitle="[green]Personal NAS Automation Platform[/]",
            border_style="bright_blue",
            expand=False,
            padding=(1, 2),
        )
    )
