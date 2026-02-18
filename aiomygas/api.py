"""MyGas API wrapper."""
from __future__ import annotations

from typing import Any

from . import queries
from .auth import AbstractMyGasAuth


class MyGasApi:
    """Class to communicate with the MyGas API."""
    _auth: AbstractMyGasAuth

    def __init__(self, auth: AbstractMyGasAuth) -> None:
        """Initialize the API and store the auth."""
        self._auth = auth

    async def async_get_client_info(self) -> dict[str, Any]:
        """Get client data."""
        query = queries.ClientV2()
        return await self._auth.async_request(query)

    async def async_get_accounts(self) -> dict[str, Any]:
        """Get accounts data."""
        query = queries.Accounts()
        return await self._auth.async_request(query)

    async def async_get_els_info(self, els_id: int) -> dict[str, Any]:
        """Get information about ELS account."""
        query = queries.ElsInfo(els_id)
        return await self._auth.async_request(query)

    async def async_get_lspu_info(self, lspu_id: int) -> dict[str, Any]:
        """Get information about LSPU account."""
        query = queries.LspuInfo(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_charges(self, lspu_id: int) -> dict[str, Any]:
        """Get charges data for account."""
        query = queries.Charges(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_payments(self, lspu_id: int) -> dict[str, Any]:
        """Get payments data for account."""
        query = queries.Payments(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_receipt(self, date_iso_short: str, email: str,
                                account_id: int, is_els: bool) -> dict[str, Any]:
        """Get receipt data for account."""
        query = queries.Receipt(date_iso_short, email, account_id, is_els)
        return await self._auth.async_request(query)

    async def async_indication_send(self, lspu_id: int, equipment_uuid: str, value: int | float,
                                    els_id: int | None = None) -> list[dict[str, Any]]:
        """Send indication for account."""
        query = queries.IndicationSend(lspu_id, equipment_uuid, value, els_id)
        return await self._auth.async_request(query)
