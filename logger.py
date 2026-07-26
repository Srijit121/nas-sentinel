import logging
import os

from rich.console import Console
from rich.logging import RichHandler

console = Console()

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sentinel.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("NASSentinel")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if imported multiple times
if logger.handlers:
    logger.handlers.clear()

# File logging (plain text)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)

# Console logging (colored)
rich_handler = RichHandler(
    console=console,
    show_path=False,
    show_time=False,
    markup=True,
)

logger.addHandler(file_handler)
logger.addHandler(rich_handler)
