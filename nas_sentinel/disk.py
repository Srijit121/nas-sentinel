"""
disk.py
NAS Sentinel Disk Monitoring Module
"""

from pathlib import Path
import subprocess


class DiskMonitor:
    """
    Represents a storage device that NAS Sentinel can monitor.
    """

    def __init__(self, device: str):
        """Initialize the monitor with a device path."""
        self.device = device

    def exists(self) -> bool:
        """Return True if the disk exists."""
        return Path(self.device).exists()

    def smart_supported(self) -> bool:
        """Return True if SMART is available on this device."""
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

    def get_smart_info(self) -> str:
        """Return the complete SMART output."""
        try:
            result = subprocess.run(
                ["smartctl", "-a", self.device],
                capture_output=True,
                text=True,
                check=False,
            )
            return result.stdout
        except FileNotFoundError:
            return ""

    def get_smart_data(self) -> dict:
        """
        Parse SMART information and return useful values.
        """

        smart = {
            "health": "Unknown",
            "temperature": "Unknown",
            "power_on_hours": "Unknown",
            "ssd_life": "N/A",
        }

        output = self.get_smart_info()

        for line in output.splitlines():

            if "SMART overall-health" in line:
                smart["health"] = line.split(":")[-1].strip()

            elif "Temperature_Celsius" in line:
                fields = line.split()
                smart["temperature"] = fields[9]

            elif "Power_On_Hours" in line:
                smart["power_on_hours"] = line.split()[-1]

            elif "SSD_Life_Left" in line:
                smart["ssd_life"] = line.split()[-1]

        return smart
