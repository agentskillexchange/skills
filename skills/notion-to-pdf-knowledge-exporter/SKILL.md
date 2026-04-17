---
name: Notion to PDF Knowledge Exporter
description: Queries Notion databases and pages via the Notion API v1, then renders
  content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images
  and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small
  for RAG ingestion.
category: Templates & Workflows
framework: Codex
verification: security_reviewed
source: https://github.com/makenotion/notion-sdk-js
tool_ecosystem:
  github_repo: makenotion/notion-sdk-js
  github_stars: 5582
  tool: '@notionhq/client'
  npm_weekly_downloads: 1182949
  license: MIT
  maintained: true
---
# Notion to PDF Knowledge Exporter
Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/notion-to-pdf-knowledge-exporter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/notion-to-pdf-knowledge-exporter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/)
