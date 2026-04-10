---
name: "PGlite Embeddable WASM Postgres for Browser and Node.js"
description: "PGlite is a WASM build of Postgres packaged as a TypeScript library that runs a full Postgres database in the browser, Node.js, Bun, and Deno. At only 3.7MB gzipped, it enables local-first applications with real SQL capabilities and no external database dependencies."
verification: security_reviewed
source: "https://github.com/electric-sql/pglite"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "electric-sql/pglite"
  github_stars: 14984
---

# PGlite Embeddable WASM Postgres for Browser and Node.js

What is PGlite?
PGlite is a lightweight, embeddable Postgres database compiled to WebAssembly by ElectricSQL. It packages a complete Postgres instance into a TypeScript client library that runs in browsers, Node.js, Bun, and Deno without requiring any external database server or dependencies. With nearly 15,000 GitHub stars, PGlite has become the go-to solution for embedding a real SQL database directly in JavaScript applications.
Core Capabilities
The @electric-sql/pglite npm package provides a full Postgres 17 implementation in approximately 3.7MB gzipped. It supports standard SQL queries, transactions, prepared statements, COPY operations, and most Postgres data types. PGlite can persist data to IndexedDB in the browser or the filesystem in Node.js, making it suitable for both ephemeral and persistent use cases. It also supports Postgres extensions including pgvector for vector similarity search, enabling AI and embedding workflows entirely in the browser.
Reactive and Real-Time Features
PGlite includes a live query system that provides reactive, real-time bindings. Applications can subscribe to query results and receive automatic updates when underlying data changes, similar to a real-time database but powered by full SQL. This makes it particularly useful for local-first applications that need to sync with remote databases.
How Agents Use PGlite
AI agents use PGlite to run SQL queries in sandboxed environments without needing access to external database servers. Common use cases include: running data analysis on user-provided CSV or JSON data by importing it into PGlite and querying with SQL, building local-first web applications with offline support, running database migrations and schema tests in CI pipelines, and creating embeddings-powered search using the pgvector extension without infrastructure overhead.
Installation and Usage
Install via npm: npm install @electric-sql/pglite. Basic usage is straightforward: import { PGlite } from "@electric-sql/pglite"; const db = new PGlite(); await db.query("SELECT 'Hello, PGlite!'");. For persistent storage in Node.js, pass a directory path: new PGlite("./my-pgdata"). In the browser, use IndexedDB: new PGlite("idb://my-database").
Extension Ecosystem
PGlite supports a growing set of Postgres extensions compiled to WASM, including pgvector for vector operations, PostGIS-lite for geospatial queries, and fuzzystrmatch for fuzzy text matching. Extensions are loaded dynamically and add minimal overhead to the base bundle size.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pglite-embeddable-wasm-postgres/)
