"""GraphQL queries for receipt."""
from .base import BaseQuery
from ..const import ATTR_DATE_ISO_SHORT, ATTR_EMAIL, ATTR_IS_ELS, ATTR_ID


class Receipt(BaseQuery):
    """GraphQL query for receipt."""
    OPERATION_NAME = "receipt"
    DATA_NAME = ("content", "url")
    QUERY = """
query receipt($dateIsoShort: String, $email: String, $isEls: Boolean!, $id: Float!) {
  receipt(dateIsoShort: $dateIsoShort, email: $email, isEls: $isEls, id: $id) {
    ok
    error
    content
    url
  }
}
"""

    def __init__(self, date_iso_short: str, email: str, account_id: int, is_els: bool) -> None:
        """Initialize."""
        self.variables = {
            ATTR_DATE_ISO_SHORT: date_iso_short,
            ATTR_EMAIL: email,
            ATTR_IS_ELS: is_els,
            ATTR_ID: account_id
        }
