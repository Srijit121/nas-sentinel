from nas_sentinel.nextcloud import NextcloudClient

client = NextcloudClient(
    server_url="http://192.168.29.54",
    username="Srijit",
    app_password="S3rv1c3s!2026",
)
status = client.move_file(
    "AutoUpload/NAS_Homelab_Architecture_Guide.pptx",
    "Documents/NAS_Homelab_Architecture_Guide.pptx",
)

print(status)
