# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2026-02-18

### Fixed

- Fixed CLI entry point (`main()` function was missing in `__main__.py`).
- Fixed CLI version import (was using obsolete `_version.py` instead of `importlib.metadata`).
- Fixed mutable class-level `variables` dict in `BaseQuery` (shared across instances).
- Fixed mutable class-level `_token` dict in `SimpleMyGasAuth` (shared across instances).
- Fixed race condition in `async_get_token()` by adding `asyncio.Lock`.
- Fixed unreachable dead code in `async_request()` and `_async_token_request()`.
- Fixed absolute imports in `lspu_info.py` (now uses relative imports like all other query modules).
- Fixed overly broad `except Exception` in `device_info.py`.
- Fixed `devices.json` loading path in `device_info.py` (was CWD-relative, now uses `__file__`).
- Fixed hardcoded fixture paths in `test_auth.py` and `test_device_info.py`.
- Fixed headers dict mutation in `async_request()` (was modifying shared `_headers` dict).
- Wrapped `aiohttp.ClientError` into `MyGasApiError`/`MyGasAuthError` in auth layer.

### Changed

- Removed obsolete `_version.py` (setuptools-scm artifact with stale version).
- Added `from __future__ import annotations` to all modules.
- Exported exceptions (`MyGasApiError`, `MyGasApiParseError`, `MyGasAuthError`) in `__init__.py`.
- Removed `unittest` (stdlib) from `requirements_test.txt`.
- Added `pytest.ini_options` with `asyncio_mode = "auto"` to `pyproject.toml`.
- Added `[project.optional-dependencies] test` to `pyproject.toml`.
- Added `devices.json` to `package-data` in `pyproject.toml`.
- Fixed Changelog URL in `pyproject.toml` (`master` → `main`).
- Updated `python-publish.yml` (correct project name, Python 3.13, trusted publishers via OIDC).
- Added CI workflow (`.github/workflows/ci.yml`).
- Updated README with badges, exceptions, CLI, development, and links sections.
- Removed unused constants (`CLIENT_LONG_LIVE_SESSION_LIFETIME`, `DEFAULT_MOBILE_USER_AGENT`) from `const.py`.
- Removed `async_get_client_info_v2` indirection in `api.py`.
- Removed dead code in `cli.py` (unreachable args check, commented-out code).

## [2.3.0] - 2024-02-27

### Changed

- async_timeout changed to asyncio.timeout.

## [2.2.1] - 2024-02-17

### Changed

- async_timeout changed to asyncio.timeout.

## [2.2.0] - 2024-01-27

### Added

- Support for `lspu` type accounts in cli.

### Changed

- Signature for some api methods to support `lspu` type accounts.

## [2.1.0] - 2024-01-21

### Added

- Added parsing for `lspu` type accounts.

## [2.0.0] - 2024-01-13

First public release.
