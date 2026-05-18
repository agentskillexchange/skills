---
name: "Snowflake Query History Extractor"
slug: "snowflake-query-history-extractor"
description: "Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting."
github_stars: 724
verification: "listed"
source: "https://github.com/snowflakedb/snowflake-connector-python"
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "snowflakedb/snowflake-connector-python"
  github_stars: 724
---

# Snowflake Query History Extractor

Extracts query history and performance metadata from Snowflake using the Snowflake Python Connector and INFORMATION_SCHEMA.QUERY_HISTORY view. Identifies expensive queries by credits consumed, data scanned, and spillage to remote storage. Exports results to a Pandas DataFrame for downstream analysis or Slack reporting.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone git@github.com:snowflakedb/snowflake-connector-python.git
- python -m pip install -U pip setuptools wheel build

Requirements and caveats from upstream:
- # Snowflake Connector for Python
- [![Build and Test](https://github.com/snowflakedb/snowflake-connector-python/actions/workflows/build_test.yml/badge.svg)](https://github.com/snowflakedb/snowflake-connector-python/actions/workflows/build_test.yml)
- [![codecov](https://codecov.io/gh/snowflakedb/snowflake-connector-python/branch/main/graph/badge.svg?token=MVKSNtnLr0)](https://codecov.io/gh/snowflakedb/snowflake-connector-python)

Basic usage or getting-started notes:
- to create a wheel package using PEP-517 build:
- shell
- Find the snowflake_connector_python*.whl package in the ./dist directory.

- Source: https://github.com/snowflakedb/snowflake-connector-python
- Extracted from upstream docs: https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snowflake-query-history-extractor/)
