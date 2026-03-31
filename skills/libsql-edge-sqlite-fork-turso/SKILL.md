---
name: "libSQL Edge-Ready SQLite Fork by Turso"
description: "libSQL is an open-source, open-contribution fork of SQLite by Turso that adds embedded replicas, server mode, and WebAssembly UDFs. This skill enables agents to work with libSQL for edge computing, serverless, and embedded database workloads."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/tursodatabase/libsql"
tool_ecosystem:
  tool: libsql
  github_repo: tursodatabase/libsql
  github_stars: 16551
  license: MIT
  maintained: true
---
# libSQL Edge-Ready SQLite Fork by Turso

libSQL is an open-source, open-contribution fork of SQLite by Turso that adds embedded replicas, server mode, and WebAssembly UDFs. This skill enables agents to work with libSQL for edge computing, serverless, and embedded database workloads.

## Overview

libSQL is an open-source fork of SQLite created and maintained by Turso that extends SQLite’s capabilities for modern application architectures. While preserving full SQLite compatibility, libSQL adds embedded replicas that sync from a remote primary, a server mode (libsql-server) that exposes SQLite over HTTP and WebSocket protocols similar to PostgreSQL or MySQL, and WebAssembly-based user-defined functions for running custom logic inside the database engine.

This skill teaches agents how to use libSQL and its client libraries for building applications that need lightweight, embedded databases with replication support. Agents learn to set up libsql-server for remote database access, configure embedded replicas that maintain a local SQLite-compatible database file synchronized with a remote primary, and use the TypeScript, Python, Rust, Go, or PHP client SDKs to interact with both local and remote databases through a unified API.

Key enhancements over stock SQLite include ALTER TABLE extensions for modifying column types and constraints (a major gap in standard SQLite), randomized ROWID generation for non-sequential primary keys, the virtual write-ahead log interface for custom WAL implementations, and the ability to pass SQL strings directly to virtual table implementations. These extensions solve practical problems that have long frustrated SQLite users building production applications.

Agents using this skill can provision and manage SQLite-compatible databases that replicate across edge locations, configure read replicas inside application processes for zero-latency local reads, and build serverless applications backed by a database that scales to zero when idle. libSQL supports Rust, JavaScript/TypeScript, Python, Go, PHP, C, and D through official and community client libraries. The project has over 15,000 GitHub stars, is MIT-licensed, and receives regular releases from the Turso team. For new projects requiring concurrent writes and bidirectional sync, Turso Database (a separate Rust rewrite) is the recommended path, while libSQL remains the stable, battle-tested choice for production workloads.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill libsql-edge-sqlite-fork-turso
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill libsql-edge-sqlite-fork-turso -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill libsql-edge-sqlite-fork-turso -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill libsql-edge-sqlite-fork-turso -a codex
```

### OpenClaw

```bash
clawhub install libsql-edge-sqlite-fork-turso
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/libsql-edge-sqlite-fork-turso/)
