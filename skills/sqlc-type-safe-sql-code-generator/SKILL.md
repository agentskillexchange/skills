---
name: "sqlc Type-Safe SQL Code Generator"
description: "sqlc is a SQL compiler that generates type-safe Go, Python, Kotlin, and TypeScript code from plain SQL queries. You write SQL, run sqlc, and get fully typed data access functions with compile-time safety — no ORM, no reflection, no runtime query building."
verification: security_reviewed
source: "https://github.com/sqlc-dev/sqlc"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sqlc-dev/sqlc"
  github_stars: 17275
---

# sqlc Type-Safe SQL Code Generator

sqlc (github.com/sqlc-dev/sqlc) is a code generation tool that takes a fundamentally different approach to database access: instead of writing code that builds SQL at runtime, you write SQL directly and let sqlc generate the type-safe code for you. The tool parses your SQL queries and database schema, then produces functions with proper input parameters and output structs that match your query results exactly.
The workflow is straightforward. You create .sql files containing your queries with annotations that name each query and specify whether it returns one row, many rows, or executes a statement. You define your database schema in SQL migration files or a schema.sql file. You run &#8220;sqlc generate&#8221; and the tool produces a complete data access layer with typed functions for each query, model structs matching your tables, and proper null handling.
sqlc supports PostgreSQL, MySQL, and SQLite as database engines. Code generation targets include Go (via sqlc-gen-go), Python (sqlc-gen-python), Kotlin (sqlc-gen-kotlin), and TypeScript (sqlc-gen-typescript), with community plugins supporting additional languages. The tool validates your SQL against the actual database schema at generation time, catching column mismatches, type errors, and syntax issues before they reach production.
For teams that prefer SQL over ORMs, sqlc eliminates the traditional trade-off between SQL control and type safety. There is no runtime overhead from query building or reflection — the generated code is as direct as hand-written database calls, but with compile-time guarantees. The tool also provides a playground at play.sqlc.dev for trying queries without local installation.
Configuration is managed through a sqlc.yaml file that specifies database engine, schema locations, query file paths, and code generation targets. sqlc supports managed databases for cloud-based schema analysis and offers a VS Code extension for inline feedback. With over 13,000 GitHub stars, an active Discord community, and backing from sponsors including Riza and Coder, sqlc has become a standard tool for Go developers working with SQL databases and is expanding rapidly to other language ecosystems.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlc-type-safe-sql-code-generator/)
