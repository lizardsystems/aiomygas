"""Exceptions for MyGas API."""
from __future__ import annotations


class MyGasApiError(Exception):
    """Base class for aiomygas errors"""


class MyGasApiParseError(MyGasApiError):
    """Exception class for aiomygas parsing errors"""


class MyGasAuthError(MyGasApiError):
    """Base class for aiomygas auth errors"""
