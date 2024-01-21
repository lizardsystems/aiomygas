"""MyGas GraphQL queries."""
from .accounts import Accounts
from .base import BaseQuery
from .charges import Charges
from .client import ClientV2
from .els_info import ElsInfo
from .indication_send import IndicationSend
from .lspu_info import LspuInfo
from .payments import Payments
from .receipt import Receipt
from .signin import SignIn

__all__ = [
    "BaseQuery",
    "ClientV2",
    "Accounts",
    "ElsInfo",
    "LspuInfo",
    "Charges",
    "Payments",
    "Receipt",
    "SignIn",
    "IndicationSend",
]
