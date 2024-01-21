import json
import unittest
from pathlib import Path
from unittest import mock
from unittest.mock import MagicMock

from aiohttp import ClientSession

from aiomygas import SimpleMyGasAuth
from aiomygas import queries
from aiomygas.api import MyGasApi
from aiomygas.const import ATTR_DATA, ATTR_OK, ATTR_ERROR

FIXTURES_PATH = Path(__file__).parent.absolute().joinpath("fixtures")


class TestMyGasApi(unittest.IsolatedAsyncioTestCase):
    """Test MyGasApi class."""

    fixtures = [
        ("ClientV2_response.json", 'ClientV2', 'async_get_client_info', [], {}),
        ("AccountsN_response.json", 'Accounts', 'async_get_accounts', [], {}),
        ("elsInfo_response.json", 'ElsInfo', 'async_get_els_info', [123456789], {}),
        ("lspuInfo_response.json", 'LspuInfo', 'async_get_lspu_info', [123456789], {}),
        ("paymentsByLspu_response.json", 'Payments', 'async_get_payments', [123456789], {}),
        ("indicationSendV4_response.json", 'IndicationSend', 'async_indication_send',
         [123456789, 123456789, "test_uuid", 123456789], {}),
    ]
    error_fixtures = [
        ("receipt_response_error.json", 'Receipt', 'async_get_receipt',
         ["2023-11-01", "test@email.ru", True, 123456789], {}),
        ("clientCharges_response_error.json", 'Charges', 'async_get_charges', [123456789], {})
    ]

    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.session = MagicMock(spec=ClientSession)
        self.auth = SimpleMyGasAuth(self.username, self.password, self.session)

    @mock.patch("aiomygas.auth.SimpleMyGasAuth.async_get_token")
    async def test_api_methods(self, mock_get_token):
        """Test api methods."""
        api = MyGasApi(self.auth)
        mock_get_token.return_value = "test_token"
        for file_name, query_name, method_name, args, kwargs in self.fixtures:
            query = getattr(queries, query_name)
            with open(FIXTURES_PATH.joinpath(file_name), encoding='utf-8') as json_file:
                json_resp = json.load(json_file)

            self.session.post.return_value.__aenter__.return_value.status = 200
            self.session.post.return_value.__aenter__.return_value.json.return_value = json_resp

            async_method = getattr(api, method_name)

            info = await async_method(*args)

            self.assertEqual(info, json_resp[ATTR_DATA][query.OPERATION_NAME][query.DATA_NAME])

    @mock.patch("aiomygas.auth.SimpleMyGasAuth.async_get_token")
    async def test_api_methods_error(self, mock_get_token):
        """Test api methods with error."""
        api = MyGasApi(self.auth)
        mock_get_token.return_value = "test_token"
        fixtures = self.fixtures + self.error_fixtures
        for file_name, query_name, method_name, args, kwargs in fixtures:
            query = getattr(queries, query_name)
            with open(FIXTURES_PATH.joinpath(file_name), encoding='utf-8') as json_file:
                json_resp = json.load(json_file)
                if "error" not in file_name:
                    json_resp[ATTR_DATA][query.OPERATION_NAME][ATTR_OK] = False
                    json_resp[ATTR_DATA][query.OPERATION_NAME][ATTR_ERROR] = "test_error"
                    json_resp[ATTR_DATA][query.OPERATION_NAME][query.DATA_NAME] = None

            self.session.post.return_value.__aenter__.return_value.status = 200
            self.session.post.return_value.__aenter__.return_value.json.return_value = json_resp

            async_method = getattr(api, method_name)

            with self.assertRaises(Exception) as cm:
                info = await async_method(*args, **kwargs)

            if "error" not in file_name:
                self.assertEqual(str(cm.exception), "test_error")
            else:
                self.assertEqual(str(cm.exception), json_resp[ATTR_DATA][query.OPERATION_NAME][ATTR_ERROR])

    @mock.patch("aiomygas.auth.SimpleMyGasAuth.async_get_token")
    async def test_api_methods_invalid_response(self, mock_get_token):
        """Test api methods with invalid response."""
        api = MyGasApi(self.auth)
        mock_get_token.return_value = "test_token"
        for file_name, query_name, method_name, args, kwargs in self.fixtures:
            query = getattr(queries, query_name)
            with open(FIXTURES_PATH.joinpath(file_name), encoding='utf-8') as json_file:
                json_resp = json.load(json_file)

                json_resp[ATTR_DATA][query.OPERATION_NAME][ATTR_OK] = True
                json_resp[ATTR_DATA][query.OPERATION_NAME][ATTR_ERROR] = None
                json_resp[ATTR_DATA][query.OPERATION_NAME][query.DATA_NAME] = None

            self.session.post.return_value.__aenter__.return_value.status = 200
            self.session.post.return_value.__aenter__.return_value.json.return_value = json_resp

            async_method = getattr(api, method_name)

            with self.assertRaises(Exception) as cm:
                info = await async_method(*args, **kwargs)

            self.assertEqual(str(cm.exception), f"Key {query.DATA_NAME} not found in response")
