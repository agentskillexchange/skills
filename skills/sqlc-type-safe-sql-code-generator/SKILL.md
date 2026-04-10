---
title: "sqlc Type-Safe SQL Code Generator"
description: "sqlc is a SQL compiler that generates type-safe Go, Python, Kotlin, and TypeScript code from plain SQL queries. You write SQL, run sqlc, and get fully typed data access functions with compile-time safety — no ORM, no reflection, no runtime query building."
slug: "sqlc-type-safe-sql-code-generator"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/sqlc-dev/sqlc"
tool_ecosystem:
  github_repo: "sqlc-dev/sqlc"
  github_stars: 17275
listed: true
---

# sqlc Type-Safe SQL Code Generator

sqlc is a SQL compiler that generates type-safe Go, Python, Kotlin, and TypeScript code from plain SQL queries. You write SQL, run sqlc, and get fully typed data access functions with compile-time safety — no ORM, no reflection, no runtime query building.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sqlc-type-safe-sql-code-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

sqlc (github.com/sqlc-dev/sqlc) is a code generation tool that takes a fundamentally different approach to database access: instead of writing code that builds SQL at runtime, you write SQL directly and let sqlc generate the type-safe code for you. The tool parses your SQL queries and database schema, then produces functions with proper input parameters and output structs that match your query results exactly.
The workflow is straightforward. You create .sql files containing your queries with annotations that name each query and specify whether it returns one row, many rows, or executes a statement. You define your database schema in SQL migration files or a schema.sql file. You run “sqlc generate” and the tool produces a complete data access layer with typed functions for each query, model structs matching your tables, and proper null handling.
sqlc supports PostgreSQL, MySQL, and SQLite as database engines. Code generation targets include Go (via sqlc-gen-go), Python (sqlc-gen-python), Kotlin (sqlc-gen-kotlin), and TypeScript (sqlc-gen-typescript), with community plugins supporting additional languages. The tool validates your SQL against the actual database schema at generation time, catching column mismatches, type errors, and syntax issues before they reach production.
For teams that prefer SQL over ORMs, sqlc eliminates the traditional trade-off between SQL control and type safety. There is no runtime overhead from query building or reflection — the generated code is as direct as hand-written database calls, but with compile-time guarantees. The tool also provides a playground at play.sqlc.dev for trying queries without local installation.
Configuration is managed through a sqlc.yaml file that specifies database engine, schema locations, query file paths, and code generation targets. sqlc supports managed databases for cloud-based schema analysis and offers a VS Code extension for inline feedback. With over 13,000 GitHub stars, an active Discord community, and backing from sponsors including Riza and Coder, sqlc has become a standard tool for Go developers working with SQL databases and is expanding rapidly to other language ecosystems.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlc-type-safe-sql-code-generator/)
