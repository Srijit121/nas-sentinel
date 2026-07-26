#!/bin/bash

set -e

PROJECT_DIR="/opt/nas-sentinel"

cd "$PROJECT_DIR"

source .venv/bin/activate

exec python sentinel.py
