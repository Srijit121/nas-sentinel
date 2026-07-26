from nas_sentinel.nextcloud import NextcloudClient

client = NextcloudClient(
    server_url="http://192.168.29.54",
    username="Srijit",
    app_password="S3rv1c3s!2026",
)

summary = client.get_user_summary()

print("\n===== Nextcloud Summary =====")
for key, value in summary.items():
    print(f"{key:15}: {value}")
