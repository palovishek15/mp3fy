import json
import os
from datetime import datetime
from config import LOGS_FILE


def _load() -> list:
    if not os.path.exists(LOGS_FILE):
        return []
    with open(LOGS_FILE, "r") as f:
        return json.load(f)


def _save(logs: list):
    with open(LOGS_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def log_download(url: str, status: str, title: str = ""):
    logs = _load()
    logs.append({
        "url": url,
        "title": title,
        "status": status,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
    _save(logs)


def get_logs() -> list:
    return _load()
