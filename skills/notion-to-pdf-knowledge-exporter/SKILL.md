---
name: "Notion to PDF Knowledge Exporter"
description: "Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion."
category: "Templates & Workflows"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "notion"  # from ase_tool_match
  github_stars: 5562  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1084242  # from ase_npm_downloads
  github_repo: "makenotion/notion-sdk-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Notion to PDF Knowledge Exporter

Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

## Overview

Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

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

- Marketplace: https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/
