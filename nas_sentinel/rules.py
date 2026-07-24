import json
from pathlib import Path


class RuleEngine:

    def __init__(self, config_file="/opt/nas-sentinel/config/file_rules.json"):

        with open(config_file, "r") as f:
            self.rules = json.load(f)

    def get_destination(self, filename):

        extension = Path(filename).suffix.lower()

        for folder, extensions in self.rules.items():

            if extension in extensions:
                return folder

        return "Others"
