from dotenv import load_dotenv
import os

from rich.table import Table

from nas_sentinel.banner import show_banner
from nas_sentinel.logger import logger, console
from nas_sentinel.nextcloud import NextcloudClient
from nas_sentinel.organizer import Organizer
from nas_sentinel.lock import InstanceLock

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

SERVER_URL = os.getenv("NEXTCLOUD_URL")
USERNAME = os.getenv("NEXTCLOUD_USERNAME")
APP_PASSWORD = os.getenv("NEXTCLOUD_APP_PASSWORD")

AUTOUPLOAD_FOLDER = "AutoUpload"


def main():
    """Main entry point for NAS Sentinel."""

    # --------------------------------------------------
    # Prevent multiple NAS Sentinel instances
    # --------------------------------------------------

    lock = InstanceLock()

    if not lock.acquire():
        return

    try:

        # --------------------------------------------------
        # Startup Banner
        # --------------------------------------------------

        show_banner()

        # --------------------------------------------------
        # Validate Configuration
        # --------------------------------------------------

        if not SERVER_URL or not USERNAME or not APP_PASSWORD:

            logger.error("Missing .env configuration.")

            send_notification(
                "NAS Sentinel",
                "Missing .env configuration.",
                priority="high",
                tags="warning",
            )

            return

        # --------------------------------------------------
        # Connect to Nextcloud
        # --------------------------------------------------

        logger.info("Connecting to Nextcloud...")

        client = NextcloudClient(
            SERVER_URL,
            USERNAME,
            APP_PASSWORD,
        )

        user = client.get_user_summary()

        logger.info(f"[green]Connected[/] : {user['display_name']}")
        logger.info(f"[cyan]Storage[/]   : {user['used_gb']} GB")

        # --------------------------------------------------
        # Organizer
        # --------------------------------------------------

        organizer = Organizer(client)

        logger.info("[bold cyan]Starting Organizer...[/]")

        summary = organizer.organize(AUTOUPLOAD_FOLDER)

        # --------------------------------------------------
        # Notifications
        # --------------------------------------------------

        if summary["failed"] > 0:

            send_notification(
                "NAS Sentinel",
                (
                    f"Processing completed\n\n"
                    f"Processed : {summary['processed']}\n"
                    f"Moved     : {summary['moved']}\n"
                    f"Skipped   : {summary['skipped']}\n"
                    f"Failed    : {summary['failed']}"
                ),
                priority="high",
                tags="warning",
            )

        elif summary["moved"] > 0:

            send_notification(
                "NAS Sentinel",
                (f"Successfully organized files.\n\n" f"Moved : {summary['moved']}"),
                priority="default",
                tags="white_check_mark",
            )

        # --------------------------------------------------
        # Summary Table
        # --------------------------------------------------

        table = Table(title="Processing Summary")

        table.add_column("Metric", style="cyan")
        table.add_column("Count", justify="right")

        table.add_row("Processed", str(summary["processed"]))
        table.add_row("Moved", str(summary["moved"]))
        table.add_row("Skipped", str(summary["skipped"]))
        table.add_row("Failed", str(summary["failed"]))

        console.print()
        console.print(table)

    except Exception as e:

        logger.exception("[red]Unexpected error[/]")

        send_notification(
            "NAS Sentinel CRITICAL",
            str(e),
            priority="urgent",
            tags="rotating_light",
        )

    finally:

        # --------------------------------------------------
        # Always release the lock
        # --------------------------------------------------

        lock.release()


if __name__ == "__main__":
    main()
