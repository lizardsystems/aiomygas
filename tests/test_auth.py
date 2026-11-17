import json
import time
import unittest
from pathlib import Path
from unittest import IsolatedAsyncioTestCase
from unittest import mock

from aiohttp import (
    ClientConnectionError,
    ClientResponseError,
    ClientSession,
    ConnectionTimeoutError,
    ContentTypeError,
)

from aiomygas.auth import SimpleMyGasAuth
from aiomygas.const import CLIENT_SESSION_LIFETIME
from aiomygas.exceptions import (
    MyGasApiParseError,
    MyGasAuthError,
    MyGasConnectionError,
)
from aiomygas.queries import ClientV2

FIXTURES_PATH = Path(__file__).parent.absolute().joinpath("fixtures")


class TestSimpleMyGasAuth(IsolatedAsyncioTestCase):
    json_fixtures = ["signInN3_response", "signInN3_response_error"]  # list of json fixtures

    def load_fixtures(self) -> dict:
        """Load a fixtures."""
        fixtures = {}
        for fixture in self.json_fixtures:
            with open(FIXTURES_PATH.joinpath(f"{fixture}.json"), encoding='utf-8') as json_file:
                fixtures[fixture] = json.load(json_file)
        return fixtures

    def setUp(self):
        """Set up test variables and fixtures."""
        self.username = "test_user"
        self.password = "test_password"
        self.session = mock.MagicMock(spec=ClientSession)
        self.auth = SimpleMyGasAuth(self.username, self.password, self.session)
        self.fixtures = self.load_fixtures()

    def test_init(self):
        """Test __init__ method."""
        self.assertEqual(self.auth._identifier, self.username)
        self.assertEqual(self.auth._password, self.password)

    def test_is_valid_token(self):
        """Test _is_valid_token method."""
        valid_token = {
            "token": "test_token",
            "expires_at": time.time()
        }
        self.assertTrue(self.auth._is_valid_token(valid_token))

        invalid_token = {
            "token": "test_token"
        }
        self.assertFalse(self.auth._is_valid_token(invalid_token))

        empty_token = {}
        self.assertFalse(self.auth._is_valid_token(empty_token))

    def test_is_expired_token(self):
        """Test _is_expired_token method."""
        expired_token = {
            "token": "test_token",
            "expires_at": time.time() - CLIENT_SESSION_LIFETIME
        }
        self.assertTrue(self.auth._is_expired_token(expired_token))

        valid_token = {
            "token": "test_token",
            "expires_at": time.time() + CLIENT_SESSION_LIFETIME
        }
        self.assertFalse(self.auth._is_expired_token(valid_token))

    async def test_async_get_token_valid(self):
        """Test async_get_token with valid token."""

        valid_token = {
            "token": "valid_test_token",
            "expires_at": time.time() + CLIENT_SESSION_LIFETIME
        }

        self.auth._token = valid_token

        token = await self.auth.async_get_token()
        self.assertEqual(token, valid_token["token"])
        self.assertTrue(self.auth._is_valid_token(self.auth._token))
        self.assertFalse(self.auth._is_expired_token(self.auth._token))

    async def test_async_get_token_expired(self):
        """Test async_get_token with expired token."""

        invalid_token = {
            "token": "invalid_test_token",
            "expires_at": time.time() - CLIENT_SESSION_LIFETIME
        }

        self.auth._token = invalid_token
        json_resp = self.fixtures["signInN3_response"]
        self.session.post.return_value.__aenter__.return_value.status = 200
        self.session.post.return_value.__aenter__.return_value.json.return_value = json_resp

        token = await self.auth.async_get_token()

        self.assertNotEqual(token, invalid_token["token"])
        self.assertEqual(token, json_resp['data']['signInN3']["token"])
        self.assertTrue(self.auth._is_valid_token(self.auth._token))
        self.assertFalse(self.auth._is_expired_token(self.auth._token))

    async def test_async_get_token_auth_error(self):
        """Test async_get_token with api error."""
        self.auth._token = {}
        error_api_response = self.fixtures["signInN3_response_error"]
        self.session.post.return_value.__aenter__.return_value.status = 200
        self.session.post.return_value.__aenter__.return_value.json.return_value = error_api_response

        with self.assertRaises(MyGasAuthError):
            token = await self.auth.async_get_token()


    async def test_async_get_token_transient_errors(self):
        """Network and HTTP failures are connection errors, not auth errors."""
        errors = [
            ClientConnectionError("DNS server returned general failure"),
            ConnectionTimeoutError("Connection timeout to host"),
            ClientResponseError(mock.MagicMock(), (), status=405, message="Not Allowed"),
            ContentTypeError(mock.MagicMock(), ()),
            TimeoutError(),
        ]
        for error in errors:
            with self.subTest(error=type(error).__name__):
                self.auth._token = {}
                self.session.post.side_effect = error
                with self.assertRaises(MyGasConnectionError) as ctx:
                    await self.auth.async_get_token()
                self.assertNotIsInstance(ctx.exception, MyGasAuthError)
                self.assertEqual(self.auth._token, {})

    async def test_async_get_token_no_signin_result(self):
        """A response without a sign-in result is a parse error, not an auth error."""
        responses = [
            {"errors": [{"message": "Internal server error"}], "data": None},
            {"data": {}},
            {"data": {"signInN3": {"ok": True, "error": None, "hasAgreement": True}}},
        ]
        for response in responses:
            with self.subTest(response=response):
                self.auth._token = {}
                self.session.post.return_value.__aenter__.return_value.json.return_value = response
                with self.assertRaises(MyGasApiParseError):
                    await self.auth.async_get_token()

    async def test_async_request_connection_error(self):
        """A network failure on a data request is a connection error."""
        self.auth._token = {
            "token": "valid_test_token",
            "expires_at": time.time() + CLIENT_SESSION_LIFETIME,
        }
        self.session.post.side_effect = ClientConnectionError("Connection reset")
        with self.assertRaises(MyGasConnectionError):
            await self.auth.async_request(ClientV2())


if __name__ == "__main__":
    unittest.main()
