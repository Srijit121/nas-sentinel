from nas_sentinel.nextcloud import NextcloudClient
from nas_sentinel.rules import RuleEngine

client = NextcloudClient(
    server_url="http://192.168.29.54",
    username="Srijit",
    app_password="S3rv1c3s!2026",
)

engine = RuleEngine()

files = client.list_directory("AutoUpload")

print("=" * 60)
print("NAS Sentinel Organization Preview")
print("=" * 60)

for filename in files:
    destination = engine.get_destination(filename)
    print(f"{filename:<50} -> {destination}")
