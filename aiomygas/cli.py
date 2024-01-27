"""Provide a CLI for TNS-Energo API."""
from __future__ import annotations

import argparse
import logging
from datetime import datetime
from pprint import pprint
from typing import Any

from aiohttp import ClientSession

from ._version import __version__
from .api import MyGasApi
from .auth import SimpleMyGasAuth
from .const import LOG_LEVELS


def get_arguments() -> argparse.Namespace:
    """Get parsed passed in arguments."""
    parser = argparse.ArgumentParser(description="Command line tool for MyGas API")
    # username and password are required positional arguments for the API
    parser.add_argument('identifier', help="User identifier (email) for MyGas API")
    parser.add_argument('password', help="password for MyGas API")
    # client_info is an optional argument to get client info
    parser.add_argument('--client', action='store_true', help="get client info")
    # accounts is an optional argument to get accounts
    parser.add_argument('--accounts', action='store_true', help="get accounts info")
    # charges is an optional argument to get charges
    parser.add_argument('--charges', action='store_true', help="get charges")
    # payments is an optional argument to get payments
    parser.add_argument('--payments', action='store_true', help="get payments")
    # receipt is an optional argument to get receipt
    parser.add_argument('--receipt', action='store_true', help="get receipt")
    # info is an optional argument to get info
    parser.add_argument('--info', action='store_true', help="get info")
    # send is an optional argument to send reading
    parser.add_argument('--send', action='store_true', help="send reading")
    # -v is a flag that can be used multiple times to increase the verbosity level
    parser.add_argument('-v', '--verbose', action='count', default=0, help="increase verbosity level")
    # -V is a flag that prints the version number
    parser.add_argument("-V", "--version", action="version", version=__version__)

    arguments = parser.parse_args()

    return arguments


async def cli() -> None:
    """Run main."""
    args = get_arguments()

    # Setup logging and the log level according to the "-v" option
    logging.basicConfig(level=LOG_LEVELS.get(args.verbose, logging.INFO))

    if not args.identifier or not args.password:
        print("Please provide username and password")
        return

    identifier = args.identifier
    password = args.password

    # create session
    async with ClientSession() as session:
        # create auth and api
        auth = SimpleMyGasAuth(identifier, password, session)
        api = MyGasApi(auth)

        # get client info for identifier
        if args.client:
            await get_client_info(api, identifier)

        # get accounts for identifier
        if args.accounts or args.charges or args.payments or args.receipt or args.info or args.send:
            print(f"Accounts for {identifier}:")
            _accounts = await api.async_get_accounts()
            pprint(_accounts)

            # get charges for each account
            if args.charges:
                await get_charges(api, identifier, _accounts)

            # get payments for each account
            if args.payments:
                await get_payments(api, identifier, _accounts)

            # get receipts for each account
            if args.receipt:
                await get_receipts(api, identifier, _accounts)

            # get info for each account
            if args.info:
                await get_info(api, identifier, _accounts)

            # send reading for each account
            if args.send:
                await send_readings(api, identifier, _accounts)


async def send_readings(api: MyGasApi, identifier: str, accounts: dict[str, Any]) -> None:
    print(f"Send readings for {identifier}:")
    if accounts.get("elsGroup"):
        for els_group in accounts["elsGroup"]:
            els = els_group['els']
            print(f"{els['id']} ({els['jntAccountNum']}):")
            if els['alias']:
                print(f"Alias: {els['alias']}")
                try:
                    _info = await api.async_get_els_info(els['id'])
                    if _info.get("lspuInfoGroup"):
                        for lspu in _info["lspuInfoGroup"]:
                            await send_readings_lspu(api, lspu, els['id'])
                    else:
                        print(f"Account {els['id']} does not have 'lspuInfoGroup' in info")
                except Exception as e:
                    print(f"Error getting info for {els['id']}: {e}")
    elif accounts.get("lspu"):
        for lspu in accounts["lspu"]:
            print(f"{lspu['id']} ({lspu['account']}):")
            if lspu['alias']:
                print(f"Alias: {lspu['alias']}")
            lspu = await api.async_get_lspu_info(lspu['id'])
            await send_readings_lspu(api, lspu)
    else:
        print("No accounts found")


async def send_readings_lspu(api: MyGasApi, lspu: dict[str, Any], els_id: int | None = None) -> None:
    """Send readings for each els account."""
    print(f"{lspu['accountId']} ({lspu['account']}):")
    if lspu['alias']:
        print(f"Alias: {lspu['alias']}")

    for counter in lspu['counters']:
        print(f"{counter['name']}:")
        values = counter.get('values', [])
        if values:
            last_readings = values[0]
            last_value = int(last_readings['valueDay'])
            print(f"Last value: {last_value}")
            print(f"Date: {last_readings['date']}")
            print(f"Status: {last_readings['state']}")
        else:
            last_value = None
            print(f"Last value: Unknown")

        value = float(input("Please enter new value: "))

        if last_value is not None and value < last_value:
            print(f"Error: New value {value} is less than last value {last_value}")
            continue
        try:
            _send = await api.async_indication_send(counter['lspuId'], counter['uuid'], value, els_id)
            print(_send[0]['counters'][0]['message'])
        except Exception as e:
            pprint(f"Error sending indication for {counter['name']}: {e}")
            print("Try sending this meter reading in 5 minutes")


async def get_info(api: MyGasApi, identifier: str, accounts: dict[str, Any]) -> None:
    """Get info for each account."""
    print(f"Info for {identifier}:")
    if accounts.get("elsGroup"):
        await get_els_info(api, accounts)
    elif accounts.get("lspu"):
        await get_lspu_info(api, accounts)
    else:
        print("No accounts found")


async def get_lspu_info(api: MyGasApi, accounts: dict[str, Any]) -> None:
    """Get info for each lspu account."""
    if accounts.get("lspu"):
        for lspu in accounts["lspu"]:
            print(f"Info for {lspu['id']} ({lspu['account']}):")
            if lspu.get('alias'):
                print(f"Alias: {lspu['alias']}")
            try:
                _info = await api.async_get_lspu_info(lspu['id'])
                pprint(_info)
            except Exception as e:
                print(f"Error getting info for {lspu['id']}: {e}")
    else:
        print(f"Account does not have 'lspu' in accounts info")


async def get_els_info(api: MyGasApi, accounts: dict[str, Any]) -> None:
    """Get info for each els account."""
    if accounts.get("elsGroup"):
        for els_group in accounts["elsGroup"]:
            print(f"Info for {els_group['els']['id']} ({els_group['els']['jntAccountNum']}):")
            if els_group['els']['alias']:
                print(f"Alias: {els_group['els']['alias']}")
            try:
                _info = await api.async_get_els_info(els_group['els']['id'])
                pprint(_info)
            except Exception as e:
                print(f"Error getting info for {els_group['els']['id']}: {e}")
    else:
        print(f"Account does not have 'elsGroup' in accounts info")


async def get_receipts(api: MyGasApi, identifier: str, accounts: dict[str, Any]) -> None:
    """Get receipt for each account."""
    day = datetime.today().replace(day=1).strftime("%Y-%m-%d")

    print(f"Receipt for {identifier}:")
    send_to_mail = input(f"Send to mail {identifier} (y/n)? ").lower() == "y"
    if send_to_mail:
        email = identifier
    else:
        email = None
    if accounts.get("elsGroup"):
        for els_group in accounts["elsGroup"]:
            print(f"Receipt for {els_group['els']['id']} ({els_group['els']['jntAccountNum']}):")
            if els_group['els']['alias']:
                print(f"Alias: {els_group['els']['alias']}")
            try:
                # for lspu in els_group["lspu"]:
                #     _receipt = await api.async_get_receipt(day, email, lspu['id'], False)
                #     pprint(_receipt)
                _receipt = await api.async_get_receipt(day, email, els_group['els']['id'], True)
                pprint(_receipt)
            except Exception as e:
                print(f"Error getting receipt for {els_group['els']['id']}: {e}")
    elif accounts.get("lspu"):
        for lspu in accounts["lspu"]:
            print(f"Receipt for {lspu['id']} ({lspu['account']}):")
            if lspu['alias']:
                print(f"Alias: {lspu['alias']}")
            try:
                _receipt = await api.async_get_receipt(day, email, lspu['id'], False)
                pprint(_receipt)
            except Exception as e:
                print(f"Error getting receipt for {lspu['id']}: {e}")
    else:
        print(f"Account does not have 'elsGroup' or 'lspu' in accounts info")


async def get_payments(api: MyGasApi, identifier: str, accounts: dict[str, Any]) -> None:
    """Get payments for each account."""
    print(f"Payments for {identifier}:")
    if accounts.get("elsGroup"):
        for els_group in accounts["elsGroup"]:
            print(f"Payments for {els_group['els']['id']} ({els_group['els']['alias']}):")
            await get_payments_lspu(api, els_group["lspu"])
    elif accounts.get("lspu"):
        await get_payments_lspu(api, accounts["lspu"])
    else:
        print(f"Account does not have 'elsGroup' or 'lspu' in accounts info")


async def get_payments_lspu(api: MyGasApi, lspu_list: list | None) -> None:
    for lspu in lspu_list:
        try:
            _payments = await api.async_get_payments(lspu["id"])
            print(f"Payments for {lspu['account']}:")
            pprint(_payments)
        except Exception as e:
            print(f"Error getting payments for {lspu['account']}: {e}")


async def get_charges(api: MyGasApi, identifier: str, accounts: dict[str, Any]) -> None:
    """Get charges for each account."""
    print(f"Charges for {identifier}:")
    if accounts.get("elsGroup"):
        for els_group in accounts["elsGroup"]:
            print(f"Charges for {els_group['els']['id']} ({els_group['els']['alias']}):")
            await get_charges_lspu(api, els_group["lspu"])
    elif accounts.get("lspu"):
        await get_charges_lspu(api, accounts["lspu"])
    else:
        print(f"Account does not have 'elsGroup' or 'lspu' in accounts info")


async def get_charges_lspu(api: MyGasApi, lspu_list: list) -> None:
    for lspu in lspu_list:
        try:
            _charges = await api.async_get_charges(lspu["id"])
            print(f"Charges for {lspu['account']}:")
            pprint(_charges)
        except Exception as e:
            print(f"Error getting charges for {lspu['account']}: {e}")


async def get_client_info(api: MyGasApi, identifier: str) -> None:
    """Get client info for identifier."""
    print(f"Client Info about {identifier}:")
    _client_info = await api.async_get_client_info()
    pprint(_client_info)
