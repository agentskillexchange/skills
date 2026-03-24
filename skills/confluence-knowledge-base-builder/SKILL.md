---
name: "Confluence Knowledge Base Builder"
description: "Connects to Confluence Cloud REST API v2 using an Atlassian API token to create, update, and search pages. Converts Markdown to Confluence Storage Format and upserts with version conflict detection. Indexes page content into a local ChromaDB vector store for RAG-powered semantic search."
category: "Library & API Reference"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/confluence-knowledge-base-builder/"
---

# Confluence Knowledge Base Builder

Connects to Confluence Cloud REST API v2 using an Atlassian API token to create, update, and search pages. Converts Markdown to Confluence Storage Format and upserts with version conflict detection. Indexes page content into a local ChromaDB vector store for RAG-powered semantic search.

## Overview

Connects to Confluence Cloud REST API v2 using an Atlassian API token to create, update, and search pages. Converts Markdown to Confluence Storage Format and upserts with version conflict detection. Indexes page content into a local ChromaDB vector store for RAG-powered semantic search.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill confluence-knowledge-base-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill confluence-knowledge-base-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill confluence-knowledge-base-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill confluence-knowledge-base-builder -a codex
```

### OpenClaw

```bash
clawhub install confluence-knowledge-base-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/confluence-knowledge-base-builder/
