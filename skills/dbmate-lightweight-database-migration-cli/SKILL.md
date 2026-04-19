---
title: "dbmate Lightweight Database Migration CLI"
description: "What is dbmate? dbmate is a lightweight, framework-agnostic database migration tool designed to keep database schemas in sync across development teams and production servers. Unlike ORM-specific migration tools, dbmate uses plain SQL files and works as a standalone CLI binary. This makes it ideal for polyglot teams writing services in different languages (Go, Node.js, Python, Ruby, PHP, Rust) who need consistent migration tooling across all projects. The tool supports PostgreSQL, MySQL, SQLite, ClickHouse, BigQuery, and Spanner. Migrations are timestamp-versioned to avoid conflicts when multiple developers create migrations simultaneously, and they run atomically inside database transactions to prevent partial migration states. How It Works dbmate reads a DATABASE_URL environment variable (or accepts it via CLI flag) and manages migration files in a ./db/migrations directory. Each migration file contains an &#8220;up&#8221; section and a &#8220;down&#8221; section written in plain SQL. Running dbmate up creates the database if it doesn&#8217;t exist and applies all pending migrations. Running dbmate rollback reverses the most recent migration. The tool automatically generates a schema.sql file after each migration, making it easy to review schema changes in git diffs. It reads .env files natively, tracks applied migrations in a schema_migrations table, and supports a --wait flag that blocks until the database server is available—useful in Docker and CI environments. Installation and Integration Install via npm ( npm install --save-dev dbmate ), Homebrew ( brew install dbmate ), or download a single binary from GitHub releases. Docker images are available at ghcr.io/amacneil/dbmate . dbmate can also be used as a Go library embedded in applications. The tool is MIT-licensed with over 6,700 GitHub stars, 344 forks, and active maintenance with commits within the last 24 hours."
source: "https://github.com/amacneil/dbmate"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "amacneil/dbmate"
  github_stars: 6801
  npm_package: "dbmate"
  npm_weekly_downloads: 99225
---

# dbmate Lightweight Database Migration CLI

What is dbmate? dbmate is a lightweight, framework-agnostic database migration tool designed to keep database schemas in sync across development teams and production servers. Unlike ORM-specific migration tools, dbmate uses plain SQL files and works as a standalone CLI binary. This makes it ideal for polyglot teams writing services in different languages (Go, Node.js, Python, Ruby, PHP, Rust) who need consistent migration tooling across all projects. The tool supports PostgreSQL, MySQL, SQLite, ClickHouse, BigQuery, and Spanner. Migrations are timestamp-versioned to avoid conflicts when multiple developers create migrations simultaneously, and they run atomically inside database transactions to prevent partial migration states. How It Works dbmate reads a DATABASE_URL environment variable (or accepts it via CLI flag) and manages migration files in a ./db/migrations directory. Each migration file contains an &#8220;up&#8221; section and a &#8220;down&#8221; section written in plain SQL. Running dbmate up creates the database if it doesn&#8217;t exist and applies all pending migrations. Running dbmate rollback reverses the most recent migration. The tool automatically generates a schema.sql file after each migration, making it easy to review schema changes in git diffs. It reads .env files natively, tracks applied migrations in a schema_migrations table, and supports a --wait flag that blocks until the database server is available—useful in Docker and CI environments. Installation and Integration Install via npm ( npm install --save-dev dbmate ), Homebrew ( brew install dbmate ), or download a single binary from GitHub releases. Docker images are available at ghcr.io/amacneil/dbmate . dbmate can also be used as a Go library embedded in applications. The tool is MIT-licensed with over 6,700 GitHub stars, 344 forks, and active maintenance with commits within the last 24 hours.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbmate-lightweight-database-migration-cli/)
