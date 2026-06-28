"""Runtime paths shared by source and packaged builds."""

from __future__ import annotations

import os
from pathlib import Path


APP_DATA_DIR_NAME = ".xhs_system"


def get_data_dir() -> Path:
    """Return the app data directory, honoring explicit env overrides."""
    configured = (os.getenv("XHS_DATA_DIR") or os.getenv("XHS_APP_DATA_DIR") or "").strip()
    if configured:
        return Path(configured).expanduser()

    # Keep the existing location for compatibility with current users.
    return Path.home() / APP_DATA_DIR_NAME


def get_logs_dir() -> Path:
    return get_data_dir() / "logs"


def get_playwright_browsers_dir() -> Path:
    configured = (os.getenv("PLAYWRIGHT_BROWSERS_PATH") or "").strip()
    if configured:
        return Path(configured).expanduser()
    return get_data_dir() / "ms-playwright"


def init_runtime_env() -> None:
    """Create runtime directories and publish paths via environment vars."""
    data_dir = get_data_dir()
    logs_dir = data_dir / "logs"
    browsers_dir = get_playwright_browsers_dir()

    data_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    browsers_dir.mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("XHS_DATA_DIR", str(data_dir))
    os.environ.setdefault("XHS_APP_DATA_DIR", str(data_dir))
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(browsers_dir))

    if os.name == "nt":
        os.environ.setdefault("PLAYWRIGHT_DOWNLOAD_HOST", "https://npmmirror.com/mirrors/playwright")
