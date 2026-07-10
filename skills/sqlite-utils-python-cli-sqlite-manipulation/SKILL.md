---
name: "sqlite-utils Python CLI for SQLite Database Manipulation"
slug: "sqlite-utils-python-cli-sqlite-manipulation"
description: "sqlite-utils is a Python CLI utility and library by Simon Willison for manipulating SQLite databases. It lets you pipe JSON, CSV, or TSV data directly into SQLite, run in-memory SQL queries against files, configure full-text search, and perform schema transformations — all from the command line."
github_stars: 2026
verification: "security_reviewed"
source: "https://github.com/simonw/sqlite-utils"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "simonw/sqlite-utils"
  github_stars: 2026
---

# sqlite-utils Python CLI for SQLite Database Manipulation

sqlite-utils is a Python CLI utility and library by Simon Willison for manipulating SQLite databases. It lets you pipe JSON, CSV, or TSV data directly into SQLite, run in-memory SQL queries against files, configure full-text search, and perform schema transformations — all from the command line.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install sqlite-utils
- brew install sqlite-utils

Requirements and caveats from upstream:
- [![Python 3.x](https://img.shields.io/pypi/pyversions/sqlite-utils.svg?logo=python&logoColor=white)](https://pypi.org/project/sqlite-utils/)
- Python CLI utility and library for manipulating SQLite databases.
- You can also import sqlite_utils and use it as a Python library like this:

Basic usage or getting-started notes:
- [Run in-memory SQL queries](https://sqlite-utils.datasette.io/en/stable/cli.html#querying-data-directly-using-an-in-memory-database), including joins, directly against data in CSV, TSV or JSON files and view the results
- [Configure SQLite full-text search](https://sqlite-utils.datasette.io/en/stable/cli.html#configuring-full-text-search) against your database tables and run search queries against them, ordered by relevance
- Run [transformations against your tables](https://sqlite-utils.datasette.io/en/stable/cli.html#transforming-tables) to make schema changes that SQLite ALTER TABLE does not directly support, such as changing the type o...

- Source: https://github.com/simonw/sqlite-utils
- Extracted from upstream docs: https://raw.githubusercontent.com/simonw/sqlite-utils/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlite-utils-python-cli-sqlite-manipulation/)
