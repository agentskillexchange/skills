# Security

## Supported versions

Security fixes are applied to the latest release on the default branch.

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting for this repository. Do not attach real screenshots, account data, access tokens, or private project adapters to a public issue.

## Screenshot boundary

The manifest validator makes no network requests. With `--check-files`, it reads path metadata only and requires every referenced image to remain below the selected repository root.

Visual QA screenshots may still contain sensitive rendered information. Use non-sensitive deterministic fixtures for repeatable review and keep real-account captures outside version control.
