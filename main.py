from rich.console import Console

from nas_sentinel.banner import show_banner
from nas_sentinel.disk import DiskMonitor

console = Console()


def main() -> None:
    """Application entry point."""

    show_banner()

    ssd = DiskMonitor("/dev/sda")
    hdd = DiskMonitor("/dev/sdb")

    console.print()

    console.print("[bold cyan]SSD[/bold cyan]")
    console.print(f"Exists : {ssd.exists()}")
    console.print(f"SMART  : {ssd.smart_supported()}")
    smart = ssd.get_smart_data()

    console.print(f"Health      : {smart['health']}")
    console.print(f"Temperature : {smart['temperature']} °C")
    console.print(f"Power Hours : {smart['power_on_hours']}")
    console.print(f"SSD Life    : {smart['ssd_life']}%")
    console.print()

    console.print("[bold cyan]HDD[/bold cyan]")
    console.print(f"Exists : {hdd.exists()}")
    console.print(f"SMART  : {hdd.smart_supported()}")


if __name__ == "__main__":
    main()
