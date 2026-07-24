"""
Nextcloud API Client
NAS Sentinel
"""

import requests
import xml.etree.ElementTree as ET
from urllib.parse import unquote


class NextcloudClient:

    def __init__(self, server_url, username, app_password):
        self.server_url = server_url.rstrip("/")
        self.username = username
        self.app_password = app_password

        self.headers = {
            "OCS-APIRequest": "true",
            "Accept": "application/json",
        }

    def move_file(self, source, destination):
        source_url = (
            f"{self.server_url}/remote.php/dav/files/" f"{self.username}/{source}"
        )

        destination_url = (
            f"{self.server_url}/remote.php/dav/files/" f"{self.username}/{destination}"
        )

        headers = {"Destination": destination_url}

        response = requests.request(
            "MOVE",
            source_url,
            auth=(self.username, self.app_password),
            headers=headers,
            timeout=10,
        )

        return response.status_code

    def get_user_info(self):
        url = f"{self.server_url}/ocs/v2.php/cloud/user"

        response = requests.get(
            url,
            auth=(self.username, self.app_password),
            headers=self.headers,
            timeout=10,
        )

        return response

    def get_user_summary(self):
        response = self.get_user_info()

        if response.status_code != 200:
            raise Exception(f"Nextcloud API Error: {response.status_code}")

        data = response.json()["ocs"]["data"]

        return {
            "username": data["id"],
            "display_name": data["display-name"],
            "storage": data["storageLocation"],
            "used_gb": round(data["quota"]["used"] / (1024**3), 2),
            "groups": data["groups"],
            "enabled": data["enabled"],
        }

    def list_directory(self, folder):
        url = f"{self.server_url}/remote.php/dav/files/{self.username}/{folder}/"

        response = requests.request(
            "PROPFIND",
            url,
            auth=(self.username, self.app_password),
            headers={"Depth": "1"},
            timeout=10,
        )

        if response.status_code != 207:
            raise Exception(f"WebDAV Error: {response.status_code}")

        namespace = {"d": "DAV:"}
        root = ET.fromstring(response.text)

        files = []

        for item in root.findall("d:response", namespace):
            href = item.find("d:href", namespace).text
            name = unquote(href.rstrip("/").split("/")[-1])

            if name == folder or name == "":
                continue

            files.append(name)

        return files

    def create_folder(self, folder):
        url = f"{self.server_url}/remote.php/dav/files/" f"{self.username}/{folder}"

        response = requests.request(
            "MKCOL",
            url,
            auth=(self.username, self.app_password),
            timeout=10,
        )

        # Folder already exists
        if response.status_code == 405:
            return True

        return response.status_code in (201, 405)
