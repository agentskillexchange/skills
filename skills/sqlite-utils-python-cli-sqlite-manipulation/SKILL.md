---
title: "sqlite-utils Python CLI for SQLite Database Manipulation"
description: "sqlite-utils is a Python command-line tool and library created by Simon Willison (creator of Datasette and Django co-creator) for working with SQLite databases. Available at github.com/simonw/sqlite-utils with extensive documentation at sqlite-utils.datasette.io, it has become a standard tool in the data engineering and analysis toolkit. The core design principle of sqlite-utils is that SQLite should be as easy to work with as a spreadsheet. You can pipe JSON data from any source directly into a new database and sqlite-utils will automatically create the table with the correct schema. The same works for CSV and TSV files. This makes it trivial to turn any data source — API responses, log files, exported spreadsheets — into a queryable SQLite database in a single command. One of the most powerful features is in-memory SQL queries against flat files. You can run sqlite-utils memory dogs.csv \"select * from t where age > 3\" to query a CSV file using SQL without ever creating a database file. This extends to joins across multiple files, aggregations, and complex queries. It supports full-text search configuration, allowing you to index text columns and run relevance-ranked search queries. For schema management, sqlite-utils provides transformation commands that work around SQLite&#8217;s limited ALTER TABLE support. You can change column types, rename columns, reorder columns, and extract normalized tables from denormalized data — operations that would normally require creating a new table, copying data, and dropping the old one. A skill built on sqlite-utils gives an AI agent a fast, flexible way to create, query, and transform structured data. The agent could ingest API responses into local databases, run analytical queries, normalize messy data, or build full-text search indexes. Install via pip install sqlite-utils or brew install sqlite-utils . The tool supports plugins for custom SQL functions and is Apache 2.0 licensed."
source: "https://github.com/simonw/sqlite-utils"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "simonw/sqlite-utils"
  github_stars: 2026
---

# sqlite-utils Python CLI for SQLite Database Manipulation

sqlite-utils is a Python command-line tool and library created by Simon Willison (creator of Datasette and Django co-creator) for working with SQLite databases. Available at github.com/simonw/sqlite-utils with extensive documentation at sqlite-utils.datasette.io, it has become a standard tool in the data engineering and analysis toolkit. The core design principle of sqlite-utils is that SQLite should be as easy to work with as a spreadsheet. You can pipe JSON data from any source directly into a new database and sqlite-utils will automatically create the table with the correct schema. The same works for CSV and TSV files. This makes it trivial to turn any data source — API responses, log files, exported spreadsheets — into a queryable SQLite database in a single command. One of the most powerful features is in-memory SQL queries against flat files. You can run sqlite-utils memory dogs.csv "select * from t where age > 3" to query a CSV file using SQL without ever creating a database file. This extends to joins across multiple files, aggregations, and complex queries. It supports full-text search configuration, allowing you to index text columns and run relevance-ranked search queries. For schema management, sqlite-utils provides transformation commands that work around SQLite&#8217;s limited ALTER TABLE support. You can change column types, rename columns, reorder columns, and extract normalized tables from denormalized data — operations that would normally require creating a new table, copying data, and dropping the old one. A skill built on sqlite-utils gives an AI agent a fast, flexible way to create, query, and transform structured data. The agent could ingest API responses into local databases, run analytical queries, normalize messy data, or build full-text search indexes. Install via pip install sqlite-utils or brew install sqlite-utils . The tool supports plugins for custom SQL functions and is Apache 2.0 licensed.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlite-utils-python-cli-sqlite-manipulation/)
