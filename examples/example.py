""" Example showing usage of this library """

import asyncio

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
        # print the accounts
        print(data)


if __name__ == "__main__":
    _email = str(input("Email: "))
    _password = str(input("Password: "))
    asyncio.run(main(_email, _password))
