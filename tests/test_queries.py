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

    def test_parse_exception_invalid(self):
        """Test parse method with empty api response."""
        self.query.OPERATION_NAME = "test"
        self.query.DATA_NAME = "test_data"
        response = {}
        with self.assertRaises(MyGasApiError) as error:
            self.query.parse(response)

        self.assertEqual(str(error.exception), "Invalid API response")
