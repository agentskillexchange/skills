---
title: "Drizzle ORM TypeScript SQL Database Toolkit"
description: "Drizzle ORM is a lightweight TypeScript ORM that provides type-safe SQL schema declarations, relational and SQL-like query builders, and automatic migration generation. At only 7.4kb minified and gzipped with zero dependencies, it supports PostgreSQL, MySQL, and SQLite including serverless databases like Neon, Turso, and Cloudflare D1."
verification: security_reviewed
source: "https://github.com/drizzle-team/drizzle-orm"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "drizzle-team/drizzle-orm"
  github_stars: 33566
  npm_package: "drizzle-orm"
  npm_weekly_downloads: 7047826
  license: "Apache-2.0"
---

# Drizzle ORM TypeScript SQL Database Toolkit

Drizzle ORM is a modern TypeScript ORM built around the principle that an ORM should be a thin, typed layer on top of SQL rather than an abstraction that hides it. Developers declare their database schemas using TypeScript code, and Drizzle provides full type inference across queries, inserts, updates, and joins. The result is compile-time safety for database operations without the overhead of code generation steps or runtime schema validation.

The library supports two complementary query styles. The SQL-like query builder maps directly to SQL concepts like select, where, join, group by, and subqueries, giving developers precise control over the generated SQL while retaining full TypeScript type safety. The relational query builder provides a higher-level API for fetching nested data across relations, similar to Prisma’s include syntax but backed by efficient SQL joins rather than multiple round trips.

Drizzle works with every major SQL database: PostgreSQL, MySQL, and SQLite, including serverless variants like Neon, PlanetScale, Turso, Cloudflare D1, Vercel Postgres, Supabase, and AWS Data API. It runs in Node.js, Bun, Deno, Cloudflare Workers, and browser environments. There are no Rust binaries or serverless adapters to configure; the library operates as pure JavaScript and connects directly to database drivers.

The companion CLI tool, Drizzle Kit, handles database migrations. It introspects the TypeScript schema files, compares them against the current database state, and generates SQL migration files or applies changes directly. This schema-as-code approach means the TypeScript schema definitions serve as both the source of truth and the migration source, eliminating drift between code and database.

Drizzle Studio provides a browser-based GUI for browsing and editing data in any connected database. The ORM weighs just 7.4kb minified and gzipped, has zero runtime dependencies, and is fully tree-shakeable. With over 33,000 GitHub stars and recognition as the top database tool in the State of DB survey, Drizzle has become one of the most widely adopted TypeScript ORMs in production use.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/drizzle-orm-typescript-sql-database-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/drizzle-orm-typescript-sql-database-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drizzle-orm-typescript-sql-database-toolkit/)
