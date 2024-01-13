"""Test device_info module."""
import unittest
from unittest.mock import mock_open, patch

from aiomygas.const import DEFAULT_DEVICE_INFO, APP_VERSION, MOBILE_APP_NAME, DEFAULT_MOBILE_BROWSER
from aiomygas.device_info import get_device_info


def device_info_fixture(filename):
    with open(f"fixtures/{filename}", encoding='utf-8') as f:
        return f.read()


class TestDeviceInfo(unittest.TestCase):
    """Test device_info module."""

    @patch('builtins.open', new_callable=mock_open,
           read_data=device_info_fixture("device_info.json")
           )
    def test_get_device_info(self, mock_file):
        """Test get_device_info method."""
        expected_device_info = {
            "appName": "mobile",
            "appVersion": APP_VERSION[MOBILE_APP_NAME],
            "browser": DEFAULT_MOBILE_BROWSER,
            "device": "Samsung A10",
            "screenResolution": "384x592",
            "system": "android"
        }
        device_info = get_device_info()
        self.assertEqual(device_info, expected_device_info)

    @patch('builtins.open', side_effect=Exception)
    def test_get_device_info_exception(self, mock_file):
        """Test get_device_info method with exception."""
        expected_device_info = DEFAULT_DEVICE_INFO
        device_info = get_device_info()
        self.assertEqual(device_info, expected_device_info)


if __name__ == "__main__":
    unittest.main()
