"""Test queries."""
from unittest import IsolatedAsyncioTestCase

from aiomygas.exceptions import MyGasApiError, MyGasApiParseError
from aiomygas.queries.base import BaseQuery


class TestBaseQuery(IsolatedAsyncioTestCase):
    """Test BaseQuery class."""

    def setUp(self):
        """Set up test variables and fixtures."""
        self.query = BaseQuery()

    def test_parse(self):
        """Test parse method."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = "test_data"
        response = {
            "data": {
                "test": {
                    "ok": True,
                    "error": None,
                    "test_data": "test_data"
                }
            }
        }
        self.assertEqual(self.query.parse(response), "test_data")

    def test_parse_exception(self):
        """Test parse method with exception."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = "test_data"
        response = {
            "data": {
                "test": {
                    "ok": False,
                    "error": "test_error",
                    "test_data": "test_data"
                }
            }
        }
        with self.assertRaises(MyGasApiError) as error:
            self.query.parse(response)

        self.assertEqual(str(error.exception), "test_error")

    def test_parse_exception_parse_error(self):
        """Test parse method with invalid response."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = "test_data"
        response = {
            "data": {
                "test": {
                    "ok": True,
                }
            }
        }
        with self.assertRaises(MyGasApiParseError) as error:
            self.query.parse(response)

    def test_parse_tuple_data_name(self):
        """Test parse method with tuple DATA_NAME."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = ("key_a", "key_b")
        response = {
            "data": {
                "test": {
                    "ok": True,
                    "error": None,
                    "key_a": "value_a",
                    "key_b": "value_b",
                }
            }
        }
        result = self.query.parse(response)
        self.assertEqual(result, {"key_a": "value_a", "key_b": "value_b"})

    def test_parse_tuple_data_name_missing_key(self):
        """Test parse method with tuple DATA_NAME and missing key."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = ("key_a", "key_b")
        response = {
            "data": {
                "test": {
                    "ok": True,
                    "error": None,
                    "key_a": "value_a",
                }
            }
        }
        with self.assertRaises(MyGasApiParseError) as error:
            self.query.parse(response)
        self.assertEqual(str(error.exception), "Key key_b not found in response")

    def test_parse_exception_invalid(self):
        """Test parse method with empty api response."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = "test_data"
        response = {}
        with self.assertRaises(MyGasApiError) as error:
            self.query.parse(response)

        self.assertEqual(str(error.exception), "Invalid API response")

    def test_to_json(self):
        """Test to_json method."""
        self.query.OPERATION_NAME = "test"
        self.query.QUERY = "query test { test { ok } }"
        self.query.variables = {"key": "value"}
        result = self.query.to_json()
        self.assertEqual(result, {
            "operationName": "test",
            "query": "query test { test { ok } }",
            "variables": {"key": "value"},
        })
