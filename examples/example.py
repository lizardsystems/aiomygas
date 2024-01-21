""" Example showing usage of this library """

import asyncio
from pprint import pprint

import aiohttp

from aiomygas import SimpleMyGasAuth, MyGasApi


async def main(email: str, password: str) -> None:
    """Create the aiohttp session and run the example."""
    async with aiohttp.ClientSession() as session:
        # create the auth
        auth = SimpleMyGasAuth(email, password, session)
        # create the api
        api = MyGasApi(auth)
        # get the accounts
        data = await api.async_get_accounts()

        # for els account
        for els in data["elsGroup"]:
            els_id = els["els"]["id"]
            els_data = await api.async_get_els_info(els_id)
            print(f"els {els_id}")
            pprint(els_data)

        # lspu account
        for lspu in data["lspu"]:
            lspu_id = lspu["id"]
            lspu_data = await api.async_get_lspu_info(lspu_id)
            print(f"lspu {lspu_id}")
            pprint(lspu_data)

        # print the accounts
        print(data)


if __name__ == "__main__":
    _email = str(input("Email: "))
    _password = str(input("Password: "))
    asyncio.run(main(_email, _password))
