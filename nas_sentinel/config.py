import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self):

        self.server_url = os.getenv("NEXTCLOUD_URL")
        self.username = os.getenv("NEXTCLOUD_USERNAME")
        self.app_password = os.getenv("NEXTCLOUD_APP_PASSWORD")
