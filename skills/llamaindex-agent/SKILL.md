---
name: "LlamaIndex Agent"
description: "LlamaIndex Agent is built around LlamaIndex framework for LLM data access. The underlying ecosystem is represented by run-llama/llama_index (47,942+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like indexes, readers, retrievers, query engines, agents, embeddings, nodes and preserving […]"
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/run-llama/llama_index"
tool_ecosystem:
  tool: llamaindex
  github_stars: 47942
  npm_weekly_downloads: 125659
  github_repo: run-llama/llama_index
  license: MIT
  maintained: true
---

# LlamaIndex Agent

LlamaIndex Agent is built around LlamaIndex framework for LLM data access. The underlying ecosystem is represented by run-llama/llama_index (47,942+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like indexes, readers, retrievers, query engines, agents, embeddings, nodes and preserving […]

## Overview

**LlamaIndex Agent** is built around LlamaIndex framework for LLM data access. The underlying ecosystem is represented by `run-llama/llama_index` (47,942+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like indexes, readers, retrievers, query engines, agents, embeddings, nodes and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to llamaindex so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on indexes, readers, retrievers, query engines, agents, embeddings, nodes, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses indexes, readers, retrievers, query engines, agents, embeddings, nodes instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as RAG pipelines, document retrieval, and LLM application composition.

Key integration points include RAG pipelines, document retrieval, and LLM application composition. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill llamaindex-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill llamaindex-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill llamaindex-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill llamaindex-agent -a codex
```

### OpenClaw

```bash
clawhub install llamaindex-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/llamaindex-agent/
