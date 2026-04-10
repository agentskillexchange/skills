---
title: "Elasticsearch MCP"
description: "Elasticsearch MCP is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by elastic/elasticsearch (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the […]"
slug: "elasticsearch-mcp"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/elasticsearch-mcp/"
---

# Elasticsearch MCP

Elasticsearch MCP is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by elastic/elasticsearch (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the […]

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
clawhub install elasticsearch-mcp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Elasticsearch MCP is built around Elasticsearch search and analytics engine. The underlying ecosystem is represented by elastic/elasticsearch (76,387+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like Query DSL, aggregations, indices, shards, mappings, cluster health and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to elasticsearch so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on Query DSL, aggregations, indices, shards, mappings, cluster health, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses Query DSL, aggregations, indices, shards, mappings, cluster health instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as full-text search, log analysis, SIEM, and analytics workloads.
Because this is exposed as an MCP skill, the tool surface is designed for agent-safe, structured calls instead of free-form shell usage. That means models can inspect schemas, call a narrow set of operations, and keep context across a longer workflow without re-implementing credentials or connection logic on every step. Key integration points include full-text search, log analysis, SIEM, and analytics workloads. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-mcp/)
