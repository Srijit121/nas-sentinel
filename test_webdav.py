from nas_sentinel.nextcloud import NextcloudClient

client = NextcloudClient(
    server_url="http://192.168.29.54",
    username="Srijit",
    app_password="S3rv1c3s!2026",
)

files = client.list_directory("AutoUpload")

print("\nFiles found:\n")

for file in files:
    print(file)
