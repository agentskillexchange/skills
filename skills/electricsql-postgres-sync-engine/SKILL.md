---
name: "ElectricSQL Real-Time Postgres Sync Engine"
description: "ElectricSQL is a read-path sync engine for PostgreSQL that handles partial replication, data delivery, and fan-out. It syncs data out of Postgres in real time using an HTTP API that integrates with CDNs, with Shapes for managing partial replication and client libraries for React and TypeScript."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/electric-sql/electric"
---
# ElectricSQL Real-Time Postgres Sync Engine

ElectricSQL is a read-path sync engine for PostgreSQL that handles partial replication, data delivery, and fan-out. It syncs data out of Postgres in real time using an HTTP API that integrates with CDNs, with Shapes for managing partial replication and client libraries for React and TypeScript.

## Overview

ElectricSQL, available at github.com/electric-sql/electric, is a sync engine that sits in front of PostgreSQL and delivers real-time data to applications. It reads from the Postgres WAL (Write-Ahead Log) to capture changes and streams them to clients over an HTTP API designed to work through CDNs and caching proxies. The project focuses exclusively on the read path — syncing data from the database to applications — leaving writes to be handled directly against PostgreSQL.

The core abstraction is Shapes, which define subsets of data that clients subscribe to. A Shape specifies a table, optional WHERE clause, and optional included relations. When a client subscribes to a Shape, ElectricSQL delivers the initial data set and then streams incremental updates as rows are inserted, updated, or deleted in the matching tables. This partial replication approach means clients only receive the data they need, reducing bandwidth and enabling efficient sync to edge devices and browsers.

Client libraries are available for TypeScript, React, and other frameworks. The React integration provides hooks like `useShape` that return live-updating query results, making it straightforward to build interfaces that reflect database state in real time without manual polling or WebSocket management. The HTTP API uses a chunked streaming protocol with cursor-based pagination, designed so that responses can be cached by CDNs and served to many clients simultaneously.

For agent skills, ElectricSQL enables agents to subscribe to database changes and react to them in real time. An agent can monitor specific tables or filtered subsets of data, receive notifications when relevant records change, and maintain a local synchronized copy of data for fast reads. This is useful for building agents that respond to database events, maintain dashboards, or coordinate workflows triggered by data changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill electricsql-postgres-sync-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill electricsql-postgres-sync-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill electricsql-postgres-sync-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill electricsql-postgres-sync-engine -a codex
```

### OpenClaw

```bash
clawhub install electricsql-postgres-sync-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/electricsql-postgres-sync-engine/)
