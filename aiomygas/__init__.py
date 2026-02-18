"""MyGas API wrapper."""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("aiomygas")
except PackageNotFoundError:
    __version__ = "0.0.0"

from .api import MyGasApi
from .auth import AbstractMyGasAuth, SimpleMyGasAuth
from .exceptions import MyGasApiError, MyGasApiParseError, MyGasAuthError

__all__ = [
    "MyGasApi",
    "AbstractMyGasAuth",
    "SimpleMyGasAuth",
    "MyGasApiError",
    "MyGasApiParseError",
    "MyGasAuthError",
    "__version__",
]
