---
name: "Translate and validate SQL across dialects with SQLGlot"
slug: "translate-and-validate-sql-across-dialects-with-sqlglot"
description: "Use SQLGlot when an agent needs to parse, transpile, or sanity-check SQL before moving queries between engines or trusting generated SQL."
github_stars: 9133
verification: "security_reviewed"
source: "https://github.com/tobymao/sqlglot"
author: "tobymao"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tobymao/sqlglot"
  github_stars: 9133
---

# Translate and validate SQL across dialects with SQLGlot

Use SQLGlot when an agent needs to parse, transpile, or sanity-check SQL before moving queries between engines or trusting generated SQL.

## Prerequisites

Python 3.8+, SQLGlot, and any agent or script that needs SQL parsing, transpilation, or validation.

## Installation

Use the upstream install or setup path that matches your environment:
- # Optionally prefix with UV=1 to use uv for the installation
- make install
- make install-dev
- make docs-serve

Requirements and caveats from upstream:
- It is a very comprehensive generic SQL parser with a robust [test suite](https://github.com/tobymao/sqlglot/blob/main/tests/). It is also quite [performant](#benchmarks), while being written purely in Python.
- # Pure python version
- Like parsing, generating SQL also requires the target dialect to be specified, otherwise the SQLGlot dialect will be used by default. For example, to transpile a query from Spark SQL to DuckDB, do parse_one(sql, diale...

Basic usage or getting-started notes:
- SQLGlot can detect a variety of [syntax errors](#parser-errors), such as unbalanced parentheses, incorrect usage of reserved keywords, and so on. These errors are highlighted and dialect incompatibilities can warn or...
- [Run Tests and Lint](#run-tests-and-lint)
- From PyPI:

- Source: https://github.com/tobymao/sqlglot
- Extracted from upstream docs: https://raw.githubusercontent.com/tobymao/sqlglot/HEAD/README.md

## Documentation

- https://sqlglot.com/sqlglot.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/translate-and-validate-sql-across-dialects-with-sqlglot/)
