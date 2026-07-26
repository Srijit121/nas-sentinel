from nas_sentinel.nextcloud import NextcloudClient
from nas_sentinel.organizer import Organizer

client = NextcloudClient(
    server_url="http://192.168.29.54",
    username="Srijit",
    app_password="S3rv1c3s!2026",
)

organizer = Organizer(client)
organizer.preview()
