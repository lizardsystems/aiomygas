"""MyGas API wrapper."""
from __future__ import annotations

from . import queries
from .auth import AbstractMyGasAuth


class MyGasApi:
    """Class to communicate with the TNS-Energo API."""
    _auth: AbstractMyGasAuth

    def __init__(self, auth: AbstractMyGasAuth):
        """Initialize the API and store the auth."""
        self._auth = auth

    async def async_get_client_info(self):
        """Get client data."""
        return await self.async_get_client_info_v2()

    async def async_get_client_info_v2(self):
        """Get client data V2."""
        query = queries.ClientV2()
        return await self._auth.async_request(query)

    async def async_get_accounts(self):
        """Get accounts data."""
        query = queries.Accounts()
        return await self._auth.async_request(query)

    async def async_get_els_info(self, els_id: int):
        """Get els data."""
        query = queries.ElsInfo(els_id)
        return await self._auth.async_request(query)

    async def async_get_lspu_info(self, lspu_id: int):
        """Get lspu data."""
        query = queries.LspuInfo(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_charges(self, lspu_id: int):
        """Get charges data."""
        query = queries.Charges(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_payments(self, lspu_id: int):
        """Get payments data."""
        query = queries.Payments(lspu_id)
        return await self._auth.async_request(query)

    async def async_get_receipt(self, date_iso_short: str, email: str, is_els: bool, els_id: int):
        """Get receipt data."""
        query = queries.Receipt(
            date_iso_short,  # 2023-11-01
            email,
            is_els,
            els_id
        )
        return await self._auth.async_request(query)

    async def async_indication_send(self, els_id: int, lspu_id: int, equipment_uuid: str, value: int | float):
        """Send indication."""
        query = queries.IndicationSend(
            els_id,
            lspu_id,
            equipment_uuid,
            value
        )
        return await self._auth.async_request(query)
