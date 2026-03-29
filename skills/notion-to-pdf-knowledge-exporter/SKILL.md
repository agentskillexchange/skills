---
name: "Notion to PDF Knowledge Exporter"
description: "Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion."
category: "Templates & Workflows"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
tool_ecosystem:
  tool: notion
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: makenotion/notion-sdk-js
  license: MIT
  maintained: true
---
# Notion to PDF Knowledge Exporter

Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

## Overview

**Notion to PDF Knowledge Exporter** is built around Notion workspace and database platform. The underlying ecosystem is represented by `makenotion/notion-sdk-js` (5,562+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like pages, databases.query, blocks.children, properties, relations, pagination and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to notion so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion. The implementation typically relies on pages, databases.query, blocks.children, properties, relations, pagination, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses pages, databases.query, blocks.children, properties, relations, pagination instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as knowledge bases, task tracking, content sync, and structured note workflows.

Key integration points include knowledge bases, task tracking, content sync, and structured note workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-to-pdf-knowledge-exporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-to-pdf-knowledge-exporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-to-pdf-knowledge-exporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-to-pdf-knowledge-exporter -a codex
```

### OpenClaw

```bash
clawhub install notion-to-pdf-knowledge-exporter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/)
