"""Exceptions for MyGas API."""
from __future__ import annotations


class MyGasApiError(Exception):
    """Base class for aiomygas errors"""


class MyGasApiParseError(MyGasApiError):
    """Exception class for aiomygas parsing errors"""


class MyGasAuthError(MyGasApiError):
    """Exception class for credentials rejected by the server"""


class MyGasConnectionError(MyGasApiError):
    """Exception class for transient network and HTTP errors"""
