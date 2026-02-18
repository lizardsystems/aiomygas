"""Provide a CLI for MyGas."""
from __future__ import annotations

import asyncio

from aiomygas.cli import cli


def main() -> None:
    """Run CLI."""
    asyncio.run(cli())


if __name__ == "__main__":
    main()
