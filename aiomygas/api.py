"""MyGas API wrapper."""
from __future__ import annotations

from typing import Any

from . import queries
from .auth import AbstractMyGasAuth


class MyGasApi:
    """Class to communicate with the TNS-Energo API."""
    _auth: AbstractMyGasAuth

    def __init__(self, auth: AbstractMyGasAuth) -> None:
        """Initialize the API and store the auth."""
        self._auth = auth

    async def async_get_client_info(self) -> dict[str, Any]:
        """Get client data."""
        return await self.async_get_client_info_v2()

    async def async_get_client_info_v2(self) -> dict[str, Any]:
        """Get client data V2."""
        query = queries.ClientV2()
        return await self._auth.async_request(query)

    async def async_get_accounts(self) -> dict[str, Any]:
        """Get accounts data."""
        query = queries.Accounts()
        return await self._auth.async_request(query)

    async def async_get_els_info(self, els_id: int) -> dict[str, Any]:
        """
        Get information about els account.
        :param els_id: els account identifier
        :return: els account information
        """
        query = queries.ElsInfo(els_id)
        return await self._auth.async_request(query)

    async def async_get_lspu_info(self, lspu_id: int) -> dict[str, Any]:
        """
        Get information about lspu account.
        :param lspu_id: lspu account identifier
        :return: lspu account information
        """
        query = queries.LspuInfo(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_charges(self, lspu_id: int) -> dict[str, Any]:
        """
        Get charges data for account.
        :param lspu_id: lspu account identifier
        :return: charges data
        """
        query = queries.Charges(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_payments(self, lspu_id: int) -> dict[str, Any]:
        """
        Get payments data for account.
        :param lspu_id: lspu account identifier
        :return: payments data
        """
        query = queries.Payments(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_receipt(self, date_iso_short: str, email: str,
                                account_id: int, is_els: bool) -> dict[str, Any]:
        """
        Get receipt data for account.
        :param date_iso_short: date in ISO short format (YYYY-MM-DD)
        :param email: email to send receipt
        :param account_id: account id (els_id or lspu_id)
        :param is_els: is els account
        :return: receipt data
        """

        query = queries.Receipt(date_iso_short, email, account_id, is_els)
        return await self._auth.async_request(query)

    async def async_indication_send(self, lspu_id: int, equipment_uuid: str, value: int | float,
                                    els_id: int | None = None) -> list[dict[str, Any]]:
        """
        Send indication for account.
        :param lspu_id: lspu account identifier
        :param equipment_uuid: equipment uuid (counter)
        :param value: indication value
        :param els_id: els account identifier (optional)
        :return: indication data
        """
        query = queries.IndicationSend(lspu_id, equipment_uuid, value, els_id)
        return await self._auth.async_request(query)
