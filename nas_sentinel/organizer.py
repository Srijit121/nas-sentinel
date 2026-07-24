from nas_sentinel.rules import RuleEngine
from nas_sentinel.logger import logger


class Organizer:

    def __init__(self, client):
        self.client = client
        self.engine = RuleEngine()

    def preview(self, folder="AutoUpload"):

        files = self.client.list_directory(folder)

        logger.info("=" * 60)
        logger.info("NAS Sentinel Preview")
        logger.info("=" * 60)

        for filename in files:

            destination = self.engine.get_destination(filename)

            if not destination:
                destination = "Uncategorized"

            logger.info(f"{filename:<45} -> {destination}")

    def organize(self, folder="AutoUpload"):

        files = self.client.list_directory(folder)

        summary = {
            "processed": 0,
            "moved": 0,
            "skipped": 0,
            "failed": 0,
        }

        if not files:
            logger.info("[yellow]AutoUpload folder is empty.[/]")
            return summary

        for filename in files:

            summary["processed"] += 1

            destination = self.engine.get_destination(filename)

            if not destination:
                logger.warning(f"[yellow]Skipping[/] {filename} (No matching rule)")
                summary["skipped"] += 1
                continue

            self.client.create_folder(destination)

            source = f"{folder}/{filename}"
            target = f"{destination}/{filename}"

            try:
                status = self.client.move_file(source, target)

                if status in (201, 204):
                    logger.info(f"[green]✓[/] {filename:<35} → [cyan]{destination}[/]")
                    summary["moved"] += 1
                else:
                    logger.error(f"[red]✗[/] {filename} ({status})")
                    summary["failed"] += 1

            except Exception as e:
                logger.exception(e)
                summary["failed"] += 1

        return summary
