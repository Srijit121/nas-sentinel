# NAS Sentinel

A Python-based monitoring toolkit for Linux NAS and homelab environments.

## Overview

NAS Sentinel is a lightweight monitoring toolkit designed to keep your Linux NAS healthy and reliable.

The first component, **NAS Watchdog**, monitors:

- ✅ System services
- ✅ Storage availability
- ✅ Disk SMART health
- ✅ Storage capacity

and sends instant notifications using **ntfy** whenever a failure or recovery is detected.

## Features

- Service Monitoring
- SMART Disk Health
- Storage Monitoring
- Push Notifications (ntfy)
- YAML Configuration
- State Tracking
- Python-based
- Linux Mint / Ubuntu Compatible

## Project Structure

```text
NAS-Sentinel/
├── watchdog.py
├── modules/
├── config/
├── logs/
├── reports/
├── state/
└── README.md
```

## Technologies

- Python 3
- Linux
- systemd
- SMART (smartctl)
- ntfy
- PyYAML
- Requests

## License

MIT License
