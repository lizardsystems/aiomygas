"""Provide a CLI for TNS-Energo API."""
from __future__ import annotations

import argparse
import logging
from datetime import datetime
from pprint import pprint

from aiohttp import ClientSession

from ._version import __version__
from .api import MyGasApi
from .auth import SimpleMyGasAuth
from .const import LOG_LEVELS


def get_arguments() -> argparse.Namespace:
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

    async with ClientSession() as session:
        auth = SimpleMyGasAuth(identifier, password, session)
        api = MyGasApi(auth)

        # get client info for identifier
        if args.client:
            print(f"Client Info about {identifier}:")
            _client_info = await api.async_get_client_info()
            pprint(_client_info)

        # get accounts for identifier
        if args.accounts:
            print(f"Accounts for {identifier}:")
            _accounts = await api.async_get_accounts()
            pprint(_accounts)
        else:
            _accounts = None

        # get charges for each account
        if args.charges:
            print(f"Charges for {identifier}:")
            if _accounts is None:
                _accounts = await api.async_get_accounts()
            for els_group in _accounts["elsGroup"]:
                print(f"Charges for {els_group['els']['id']} ({els_group['els']['alias']}):")
                for lspu in els_group["lspu"]:
                    try:
                        _charges = await api.async_get_charges(lspu["id"])
                        print(f"Charges for {lspu['account']}:")
                        pprint(_charges)
                    except Exception as e:
                        print(f"Error getting charges for {lspu['account']}: {e}")

        # get payments for each account
        if args.payments:
            print(f"Payments for {identifier}:")
            if _accounts is None:
                _accounts = await api.async_get_accounts()
            for els_group in _accounts["elsGroup"]:
                print(f"Payments for {els_group['els']['id']} ({els_group['els']['alias']}):")
                for lspu in els_group["lspu"]:
                    try:
                        _payments = await api.async_get_payments(lspu["id"])
                        print(f"Payments for {lspu['account']}:")
                        pprint(_payments)
                    except Exception as e:
                        print(f"Error getting payments for {lspu['account']}: {e}")

        # get receipt for each account
        if args.receipt:
            print(f"Receipt for {identifier}:")
            if _accounts is None:
                _accounts = await api.async_get_accounts()
            for els_group in _accounts["elsGroup"]:
                print(f"Receipt for {els_group['els']['id']} ({els_group['els']['alias']}):")
                try:
                    today = datetime.today().strftime("%Y-%m-%d")
                    _receipt = await api.async_get_receipt(today, identifier, True, els_group['els']['id'])
                except Exception as e:
                    print(f"Error getting receipt for {els_group['els']['id']}: {e}")

        # get info for each account
        if args.info:
            print(f"Info for {identifier}:")
            if _accounts is None:
                _accounts = await api.async_get_accounts()
            for els_group in _accounts["elsGroup"]:
                print(f"Info for {els_group['els']['id']} ({els_group['els']['alias']}):")
                try:
                    _info = await api.async_get_els_info(els_group['els']['id'])
                    pprint(_info)
                except Exception as e:
                    print(f"Error getting info for {els_group['els']['id']}: {e}")

        # send reading for each account
        if args.send:
            print(f"Send readings for {identifier}:")
            if _accounts is None:
                _accounts = await api.async_get_accounts()
            for els_group in _accounts["elsGroup"]:
                els_id = els_group['els']['id']
                try:
                    _info = await api.async_get_els_info(els_id)
                except Exception as e:
                    print(f"Error getting info for {els_id}: {e}")

                print(f"{els_group['els']['alias']} ({els_group['els']['jntAccountNum']}):")
                for lspu in _info['lspuInfoGroup']:
                    for counter in lspu['counters']:
                        print(f"{counter['name']}:")
                        values = counter.get('values', [])
                        if values:
                            last_value = float(values[0]['value'])
                            print(f"Last value: {last_value}")
                            print(f"Date: {values[0]['date']}")
                            print(f"Status: {values[0]['state']}")
                        else:
                            last_value = None
                            print(f"Last value: Unknown")

                        value = float(input("Please enter new value: "))

                        if last_value is not None and value < last_value:
                            print(f"Error: New value {value} is less than last value {last_value}")
                            continue
                        try:
                            _send = await api.async_indication_send(
                                els_id,
                                counter['lspuId'],
                                counter['uuid'],
                                value
                            )
                            print(_send[0]['counters'][0]['message'])
                        except Exception as e:
                            pprint(f"Error sending indication for {counter['name']}: {e}")
                            print("Try sending this meter reading in 5 minutes")
