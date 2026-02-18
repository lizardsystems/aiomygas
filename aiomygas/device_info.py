"""Device info."""
from __future__ import annotations

import json
from pathlib import Path
from random import choice
from typing import Any

from .const import DEFAULT_DEVICE_INFO, APP_VERSION, ATTR_BROWSER, ATTR_SYSTEM, ATTR_SCREEN_RESOLUTION, \
    ATTR_DEVICE, ATTR_APP_VERSION, ATTR_APP_NAME

_DEVICES_FILE = Path(__file__).parent / "devices.json"


def get_device_info() -> dict[str, Any]:
    """Get device info."""
    try:
        with open(_DEVICES_FILE, encoding="utf-8") as f:
            devices = json.load(f)
            app_name = choice(list(devices))
            system = choice(list(devices[app_name]))
            device_info = {
                ATTR_APP_NAME: app_name,
                ATTR_APP_VERSION: APP_VERSION[app_name],
                ATTR_BROWSER: choice(devices[app_name][system][ATTR_BROWSER]),
                ATTR_DEVICE: choice(devices[app_name][system][ATTR_DEVICE]),
                ATTR_SCREEN_RESOLUTION: choice(devices[app_name][system][ATTR_SCREEN_RESOLUTION]),
                ATTR_SYSTEM: system
            }
    except (OSError, json.JSONDecodeError, KeyError, IndexError):
        device_info = DEFAULT_DEVICE_INFO
    return device_info


DEVICE_INFO = get_device_info()
