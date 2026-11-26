# Contributing

Install `.[dev]` in a virtual environment and run `pytest -q` plus
`python src/chronicle/capture.py selftest`. Keep the capture core compatible with Python
3.9 and free of third-party imports.

Preserve append-only history, exclusion before reading sensitive paths, additive hook
installation, and labels on inferred entries. Use synthetic test data; never attach a
real ledger or transcript to an issue.
