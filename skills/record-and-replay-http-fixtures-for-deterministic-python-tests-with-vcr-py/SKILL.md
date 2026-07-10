---
name: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
slug: "record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py"
description: "Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop."
github_stars: 2956
verification: "security_reviewed"
source: "https://github.com/kevin1024/vcrpy"
author: "Kevin1024 and contributors"
publisher_type: "Open Source Project"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "kevin1024/vcrpy"
  github_stars: 2956
---

# Record and replay HTTP fixtures for deterministic Python tests with VCR.py

Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop.

## Prerequisites

Python plus VCR.py integrated into the project's test framework

## Installation

Requirements and caveats from upstream:
- |PyPI| |Python versions| |Build Status| |CodeCov| |Gitter|
- This is a Python version of Ruby's VCR
- :target: https://pypi.python.org/pypi/vcrpy

Basic usage or getting-started notes:
- first time you run code that is inside a VCR.py context manager or
- recognizes from the original test run and return the responses that
- to do is delete your existing cassette files, and run your tests again.

- Source: https://github.com/kevin1024/vcrpy
- Extracted from upstream docs: https://raw.githubusercontent.com/kevin1024/vcrpy/HEAD/README.rst

## Documentation

- https://vcrpy.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
