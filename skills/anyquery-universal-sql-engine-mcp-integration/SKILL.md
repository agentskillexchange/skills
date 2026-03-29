---
name: "Anyquery Universal SQL Engine with MCP Integration"
description: "Anyquery is a SQL query engine that lets you run SQL against 40+ apps, files, and databases including GitHub, Notion, Chrome, and Apple Notes. Built on SQLite with MCP server support for connecting AI agents to structured data across services."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/julien040/anyquery"
---
# Anyquery Universal SQL Engine with MCP Integration

Anyquery is a SQL query engine that lets you run SQL against 40+ apps, files, and databases including GitHub, Notion, Chrome, and Apple Notes. Built on SQLite with MCP server support for connecting AI agents to structured data across services.

## Overview

Anyquery is an open-source SQL query engine created by Julien Partenay that extends SQLite to query virtually any data source through a plugin system. With over 1,600 GitHub stars and active development including regular releases, it supports querying files (CSV, JSON, Parquet), databases (PostgreSQL, MySQL), and applications (GitHub, Notion, Chrome bookmarks, Todoist, Apple Notes, and 40+ more) using standard SQL syntax.

The tool’s architecture builds on SQLite’s virtual table mechanism, using plugins to bridge external data sources into queryable tables. Developers install plugins for their target services, then write standard SQL queries that join, filter, and aggregate data across completely different platforms. For example, a single query can correlate GitHub issues with Notion tasks or join Chrome bookmarks with local CSV files. Alternative query languages including PRQL and PQL are also supported.

Anyquery includes a built-in MCP server that exposes all installed data sources as tools accessible to AI agents. Running anyquery mcp –stdio starts the server in stdio mode for local AI clients, while anyquery mcp –host 127.0.0.1 –port 8070 provides HTTP+SSE access for remote connections. It also supports direct integration with ChatGPT, TypingMind, and other function-calling LLM clients through the anyquery gpt command, which generates a shareable connection ID.

Beyond querying, Anyquery can act as a MySQL-compatible server with anyquery server, allowing connections from any MySQL client including TablePlus, Metabase, DBeaver, and programmatic access through standard MySQL drivers. Installation is available via Homebrew, APT, YUM/DNF, Scoop, Winget, and Chocolatey, plus binary downloads from GitHub Releases. The project is written in Go, licensed under AGPL-3.0, and maintains comprehensive documentation at anyquery.dev.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill anyquery-universal-sql-engine-mcp-integration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill anyquery-universal-sql-engine-mcp-integration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill anyquery-universal-sql-engine-mcp-integration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill anyquery-universal-sql-engine-mcp-integration -a codex
```

### OpenClaw

```bash
clawhub install anyquery-universal-sql-engine-mcp-integration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/anyquery-universal-sql-engine-mcp-integration/)
