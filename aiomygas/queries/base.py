"""Base class fro GraphQL queries."""
from abc import ABC
from typing import Any

from ..const import ATTR_ERROR, ATTR_OK, ATTR_DATA, ATTR_VARIABLES, ATTR_QUERY, ATTR_OPERATION_NAME
from ..exceptions import MyGasApiParseError, MyGasApiError


class BaseQuery(ABC):
    """Base class fro GraphQL queries."""
    OPERATION_NAME: str
    DATA_NAME: str | tuple
    QUERY: str
    variables: dict[str, Any] = {}

    def parse(self, response: dict[str, Any]) -> Any:
        """Parse response."""
        operation = response.get(ATTR_DATA, {}).get(self.OPERATION_NAME, {})
        ok = operation.get(ATTR_OK, False)
        error = operation.get(ATTR_ERROR)
        if ok:
            if isinstance(self.DATA_NAME, str):
                data = operation.get(self.DATA_NAME)
                if data is None:
                    raise MyGasApiParseError(f"Key {self.DATA_NAME} not found in response")
            else:
                data = {}
                for data_name in self.DATA_NAME:
                    if data_name in operation:
                        data[data_name] = operation.get(data_name)
                    else:
                        raise MyGasApiParseError(f"Key {data_name} not found in response")
            return data
        else:
            raise MyGasApiError(error or "Invalid API response")

    def to_json(self) -> dict[str, Any]:
        """Return the payload."""
        return {
            ATTR_OPERATION_NAME: self.OPERATION_NAME,
            ATTR_QUERY: self.QUERY,
            ATTR_VARIABLES: self.variables
        }
