import requests

TOPIC = "your-topic-name"

NTFY_URL = f"https://ntfy.sh/{TOPIC}"


def send_notification(title, message, priority="default", tags=None):
    headers = {
        "Title": title,
        "Priority": priority,
    }

    if tags:
        headers["Tags"] = tags

    requests.post(
        NTFY_URL,
        data=message.encode("utf-8"),
        headers=headers,
        timeout=10,
    )
