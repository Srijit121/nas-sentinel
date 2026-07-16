"""
Disk Monitoring Module
NAS Sentinel
"""

from pathlib import Path
import subprocess


class DiskMonitor:
    """Monitor storage devices."""

    def __init__(self, device: str):
        self.device = device

    def exists(self) -> bool:
        """Check whether the disk exists."""
        return Path(self.device).exists()

    def smart_supported(self) -> bool:
        """Check whether SMART is supported."""

        try:
            result = subprocess.run(
                ["smartctl", "-i", self.device],
                capture_output=True,
                text=True,
                check=False,
            )

            return "SMART support is: Available" in result.stdout

        except FileNotFoundError:
            return False
