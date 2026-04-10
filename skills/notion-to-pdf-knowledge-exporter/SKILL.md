---
title: "Notion to PDF Knowledge Exporter"
description: "Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion."
slug: "notion-to-pdf-knowledge-exporter"
category:
  - "Templates &amp; Workflows"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/"
listed: true
---

# Notion to PDF Knowledge Exporter

Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

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
clawhub install notion-to-pdf-knowledge-exporter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Notion to PDF Knowledge Exporter is built around Notion workspace and database platform. The underlying ecosystem is represented by makenotion/notion-sdk-js (5,562+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like pages, databases.query, blocks.children, properties, relations, pagination and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to notion so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion. The implementation typically relies on pages, databases.query, blocks.children, properties, relations, pagination, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses pages, databases.query, blocks.children, properties, relations, pagination instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as knowledge bases, task tracking, content sync, and structured note workflows.
Key integration points include knowledge bases, task tracking, content sync, and structured note workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/)
