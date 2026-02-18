"""MyGas API Auth wrapper."""
from __future__ import annotations

import asyncio
import time
from abc import ABC, abstractmethod
from typing import Any, cast

from aiohttp import ClientError, ClientSession, hdrs

from . import queries
from .const import LOGGER, CLOCK_OUT_OF_SYNC_MAX_SEC, HEADER_TOKEN, CLIENT_SESSION_LIFETIME, \
    DEFAULT_ENDPOINT, DEFAULT_HOST, DEFAULT_ORIGIN, DEFAULT_REFERER, DEFAULT_MOBILE_BROWSER, ATTR_EXPIRES_AT, \
    ATTR_TOKEN, ATTR_BROWSER
from .device_info import DEVICE_INFO
from .exceptions import MyGasAuthError, MyGasApiError, MyGasApiParseError


class AbstractMyGasAuth(ABC):
    """Abstract class to make authenticated requests."""
    _session: ClientSession
    _endpoint: str
    _headers: dict[str, str]

    def __init__(self, session: ClientSession):
        """Initialize the auth."""
        self._session = session
        self._endpoint = DEFAULT_ENDPOINT

        self._headers = {
            hdrs.HOST: DEFAULT_HOST,
            hdrs.USER_AGENT: DEVICE_INFO[ATTR_BROWSER]
        }
        if DEVICE_INFO[ATTR_BROWSER] != DEFAULT_MOBILE_BROWSER:
            self._headers.update({
                hdrs.ORIGIN: DEFAULT_ORIGIN,
                hdrs.REFERER: DEFAULT_REFERER,
            })

    @abstractmethod
    async def async_get_token(self) -> str:
        """Return a valid access token."""

    async def async_request(self, query: queries.BaseQuery) -> Any:
        """Make a request with token authorization."""
        headers = {**self._headers, HEADER_TOKEN: await self.async_get_token()}
        payload = query.to_json()
        LOGGER.debug("Request with payload =%s, headers=%s", payload, headers)
        try:
            async with self._session.post(
                self._endpoint, json=payload, headers=headers, raise_for_status=True,
            ) as resp:
                r = await resp.json()
                LOGGER.debug("Response: %s", r)
                return query.parse(r)
        except ClientError as err:
            raise MyGasApiError(f"HTTP request failed: {err}") from err


class SimpleMyGasAuth(AbstractMyGasAuth):
    """Simple implementation of AbstractMyGasAuth."""
    _identifier: str
    _password: str

    def __init__(self,
                 identifier: str,
                 password: str,
                 session: ClientSession) -> None:
        """Initialize the auth."""
        super().__init__(session)
        self._identifier = identifier
        self._password = password
        self._token: dict[str, Any] = {}
        self._lock = asyncio.Lock()

    async def _async_token_request(self) -> dict[str, Any]:
        """Make a token request."""
        LOGGER.debug("Token request for %s", self._identifier)
        query = queries.SignIn(self._identifier, self._password)
        payload = query.to_json()
        try:
            async with self._session.post(
                self._endpoint, json=payload, headers=self._headers, raise_for_status=True,
            ) as resp:
                r = await resp.json()
                LOGGER.debug("Response: %s", r)
                try:
                    response = query.parse(r)
                    token = response[ATTR_TOKEN]
                    expires_at = time.time() + CLIENT_SESSION_LIFETIME
                    LOGGER.debug("Token request finished token = %s expires at %s", token, expires_at)
                    return {
                        ATTR_TOKEN: token,
                        ATTR_EXPIRES_AT: expires_at
                    }
                except MyGasApiError as e:
                    raise MyGasAuthError(e) from e
        except ClientError as err:
            raise MyGasAuthError(f"Token request failed: {err}") from err

    @staticmethod
    def _is_valid_token(token: dict[str, Any]) -> bool:
        """Check if token is valid and contains all required fields."""
        if token and isinstance(token, dict):
            return {ATTR_TOKEN, ATTR_EXPIRES_AT} <= token.keys()
        return False

    @staticmethod
    def _is_expired_token(token: dict[str, Any]) -> bool:
        """Check if token is expired."""
        return (
                cast(float, token.get(ATTR_EXPIRES_AT, 0))
                < time.time() + CLOCK_OUT_OF_SYNC_MAX_SEC
        )

    async def async_get_token(self) -> str:
        """Get access token."""
        async with self._lock:
            if not self._is_valid_token(self._token) or self._is_expired_token(self._token):
                self._token = await self._async_token_request()

        return self._token[ATTR_TOKEN]
