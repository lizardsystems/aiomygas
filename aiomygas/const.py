"""Constants for MyGas API."""
from __future__ import annotations

import logging
from typing import Final

LOGGER = logging.getLogger(__package__)

LOG_LEVELS = {
    None: logging.WARNING,  # 0
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}

CLIENT_SESSION_LIFETIME = 525600
CLIENT_LONG_LIVE_SESSION_LIFETIME = 365

DEFAULT_HOST = "xn--80afnfom.xn--80ahmohdapg.xn--80asehdb"
DEFAULT_ENDPOINT = f"https://{DEFAULT_HOST}/abr-lka-backend"
DEFAULT_ORIGIN = f"https://{DEFAULT_HOST}"
DEFAULT_REFERER = f"https://{DEFAULT_HOST}/"
DEFAULT_MOBILE_USER_AGENT = "Dart/2.19 (dart:io)"
DEFAULT_MOBILE_BROWSER = "App"
CLOCK_OUT_OF_SYNC_MAX_SEC = 20
HEADER_TOKEN: Final = "token"

MOBILE_APP_NAME = "mobile"
DESKTOP_APP_NAME = "desktop"
APP_VERSION = {
    MOBILE_APP_NAME: "7.5.14",
    DESKTOP_APP_NAME: "7.5.15"
}
DEFAULT_DEVICE_INFO = {
    "appName": "mobile",
    "appVersion": APP_VERSION[MOBILE_APP_NAME],
    "browser": DEFAULT_MOBILE_BROWSER,
    "device": "Samsung Galaxy S10",
    "screenResolution": "384x592",
    "system": "Android"
}
ATTR_ERROR = "error"
ATTR_OK = "ok"
ATTR_DATA = "data"
ATTR_VARIABLES = "variables"
ATTR_QUERY = "query"
ATTR_OPERATION_NAME = "operationName"
ATTR_LSPU_ID = 'lspuId'
ATTR_ELS_ID = "elsId"
ATTR_EXPIRES_AT = "expires_at"
ATTR_TOKEN = 'token'
ATTR_BROWSER = "browser"
ATTR_SYSTEM = "system"
ATTR_SCREEN_RESOLUTION = "screenResolution"
ATTR_DEVICE = "device"
ATTR_APP_VERSION = "appVersion"
ATTR_APP_NAME = "appName"
ATTR_DEVICE_INFO = 'deviceInfo'
ATTR_DATE_ISO_SHORT = 'dateIsoShort'
ATTR_EMAIL = 'email'
ATTR_IS_ELS = 'isEls'
ATTR_ID = 'id'
