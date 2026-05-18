---
name: "dbmate Lightweight Database Migration CLI"
slug: "dbmate-lightweight-database-migration-cli"
description: "dbmate is a standalone, framework-agnostic database migration tool that uses plain SQL files. It supports PostgreSQL, MySQL, SQLite, ClickHouse, BigQuery, and Spanner, and works with any programming language or framework."
github_stars: 6801
verification: "security_reviewed"
source: "https://github.com/amacneil/dbmate"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "amacneil/dbmate"
  github_stars: 6801
  npm_package: "dbmate"
  npm_weekly_downloads: 99225
---

# dbmate Lightweight Database Migration CLI

dbmate is a standalone, framework-agnostic database migration tool that uses plain SQL files. It supports PostgreSQL, MySQL, SQLite, ClickHouse, BigQuery, and Spanner, and works with any programming language or framework.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install --save-dev dbmate
- npx dbmate --help
- brew install dbmate
- Docker images are published to GitHub Container Registry ([ghcr.io/amacneil/dbmate](https://ghcr.io/amacneil/dbmate)).

Requirements and caveats from upstream:
- It is a standalone command line tool that can be used with Go, Node.js, Python, Ruby, PHP, Rust, C++, or any other language or framework you are using to write database-backed applications. This is especially helpful...
- **Docker**
- Remember to set --network=host or see [this comment](https://github.com/amacneil/dbmate/issues/128#issuecomment-615924611) for more tips on using dbmate with docker networking):

Basic usage or getting-started notes:
- [Usage](#usage)
- Migrations are run atomically inside a transaction
- **NPM**

- Source: https://github.com/amacneil/dbmate
- Extracted from upstream docs: https://raw.githubusercontent.com/amacneil/dbmate/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbmate-lightweight-database-migration-cli/)
