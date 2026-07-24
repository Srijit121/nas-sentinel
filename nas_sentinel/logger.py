import logging
import os
from logging.handlers import RotatingFileHandler

from rich.console import Console
from rich.logging import RichHandler

# ----------------------------
# Console
# ----------------------------

console = Console()

# ----------------------------
# Log Configuration
# ----------------------------

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sentinel.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("NASSentinel")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if logger.hasHandlers():
    logger.handlers.clear()

# ----------------------------
# File Logger (Rotating)
# ----------------------------

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
    encoding="utf-8",
)

file_handler.setLevel(logging.INFO)

file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)

# ----------------------------
# Rich Console Logger
# ----------------------------

rich_handler = RichHandler(
    console=console,
    show_time=False,
    show_path=False,
    markup=True,
)

rich_handler.setLevel(logging.INFO)

# ----------------------------
# Attach Handlers
# ----------------------------

logger.addHandler(file_handler)
logger.addHandler(rich_handler)
