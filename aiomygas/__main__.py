"""Provide a CLI for MyGas."""
from __future__ import annotations

import asyncio

from aiomygas.cli import cli

if __name__ == "__main__":
    asyncio.run(cli())
