"""GraphQL queries for sign-in."""
from .base import BaseQuery
from ..const import ATTR_DEVICE_INFO
from ..device_info import DEVICE_INFO


class SignIn(BaseQuery):
    """GraphQL query for sign-in."""
    OPERATION_NAME = "signInN3"
    DATA_NAME = ("token", "hasAgreement")
    QUERY = """
mutation signInN3($input: ClientSignInInputV2!, $deviceInfo: DeviceInfoInputV2!) {
  signInN3(input: $input, deviceInfo: $deviceInfo) {
    ok
    error
    token
    hasAgreement
  }
}
"""

    def __init__(self, identifier: str, password: str) -> None:
        """Initialize."""
        self.variables = {
            'input': {
                "agreement": False,
                "identifier": identifier,
                "password": password,
                "rememberMe": True
            },
            ATTR_DEVICE_INFO: DEVICE_INFO
        }
