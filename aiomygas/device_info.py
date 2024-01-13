"""Device info."""
import json
from random import choice
from typing import Any

from .const import DEFAULT_DEVICE_INFO, APP_VERSION, ATTR_BROWSER, ATTR_SYSTEM, ATTR_SCREEN_RESOLUTION, \
    ATTR_DEVICE, ATTR_APP_VERSION, ATTR_APP_NAME


def get_device_info() -> dict[str, Any]:
    """Get device info."""
    try:
        with open('devices.json', 'r') as f:
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
    except Exception as e:  # noqa
        device_info = DEFAULT_DEVICE_INFO
    return device_info


DEVICE_INFO = get_device_info()
