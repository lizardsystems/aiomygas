# aiomygas

[![PyPI](https://img.shields.io/pypi/v/aiomygas)](https://pypi.org/project/aiomygas/)
[![Python](https://img.shields.io/pypi/pyversions/aiomygas)](https://pypi.org/project/aiomygas/)
[![License](https://img.shields.io/pypi/l/aiomygas)](https://github.com/lizardsystems/aiomygas/blob/main/LICENSE)
[![CI](https://github.com/lizardsystems/aiomygas/actions/workflows/ci.yml/badge.svg)](https://github.com/lizardsystems/aiomygas/actions/workflows/ci.yml)

Asynchronous Python API for [Мой Газ](https://мойгаз.смородина.онлайн/).

## Installation

Use pip to install the library:

```commandline
pip install aiomygas
```

## Usage

```python
import asyncio
from pprint import pprint

import aiohttp

from aiomygas import SimpleMyGasAuth, MyGasApi


async def main(email: str, password: str) -> None:
    """Create the aiohttp session and run the example."""
    async with aiohttp.ClientSession() as session:
        auth = SimpleMyGasAuth(email, password, session)
        api = MyGasApi(auth)

        data = await api.async_get_accounts()

        pprint(data)


if __name__ == "__main__":
    _email = str(input("Email: "))
    _password = str(input("Password: "))
    asyncio.run(main(_email, _password))
```

## Exceptions

All exceptions inherit from `MyGasApiError`:

- `MyGasApiError` — base class for all API errors
- `MyGasApiParseError` — response parsing errors
- `MyGasAuthError` — authentication errors

## Timeouts

aiomygas does not specify any timeouts for any requests. You will need to specify them in your own code. We recommend `asyncio.timeout`:

```python
import asyncio

async with asyncio.timeout(10):
    data = await api.async_get_accounts()
```

## CLI

```commandline
aiomygas-cli user@example.com password --accounts
aiomygas-cli user@example.com password --client
aiomygas-cli user@example.com password --charges
aiomygas-cli user@example.com password --payments
aiomygas-cli user@example.com password --info
```

## Development

```commandline
python -m venv .venv
.venv/bin/pip install -r requirements_test.txt -e .
pytest tests/ -v
```

## Links

- [PyPI](https://pypi.org/project/aiomygas/)
- [GitHub](https://github.com/lizardsystems/aiomygas)
- [Changelog](https://github.com/lizardsystems/aiomygas/blob/main/CHANGELOG.md)
- [Bug Tracker](https://github.com/lizardsystems/aiomygas/issues)
