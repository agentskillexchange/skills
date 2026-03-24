---
name: "Firecrawl Markdown Capture Pipeline"
description: "Captures clean site content through Firecrawl endpoints like `/v1/scrape`, `/v1/map`, and `/v1/crawl`, with Markdown output for downstream agents. Great for turning messy websites into reliable research corpora, docs snapshots, or retrieval-ready source material."
category: "Research & Scraping"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/firecrawl-markdown-capture-pipeline/"
---

# Firecrawl Markdown Capture Pipeline

Captures clean site content through Firecrawl endpoints like `/v1/scrape`, `/v1/map`, and `/v1/crawl`, with Markdown output for downstream agents. Great for turning messy websites into reliable research corpora, docs snapshots, or retrieval-ready source material.

## Overview

Firecrawl Markdown Capture Pipeline is aimed at teams that want readable web content, not just raw DOM snapshots. It uses Firecrawl APIs such as `/v1/scrape`, `/v1/map`, and `/v1/crawl` to discover pages, fetch them with browser-aware rendering, and transform the results into Markdown that is much easier to store, diff, summarize, and index. That makes it a strong fit for research systems, internal knowledge bases, and agent workflows that need high-quality source text.

The skill can separate sitemap discovery from deep crawling, control which pages get expanded, and preserve page-level metadata so downstream tools know where each document originated. Compared with ad hoc scraping, that reduces cleanup time and makes the corpus more suitable for retrieval, summarization, and change tracking. It is also useful when sites rely on JavaScript rendering that simpler HTTP fetchers miss or fragment badly.

Use this skill when your priority is clean page capture in Markdown, controlled crawl coverage, and a pipeline that turns live websites into durable, machine-friendly research assets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill firecrawl-markdown-capture-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill firecrawl-markdown-capture-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill firecrawl-markdown-capture-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill firecrawl-markdown-capture-pipeline -a codex
```

### OpenClaw

```bash
clawhub install firecrawl-markdown-capture-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/firecrawl-markdown-capture-pipeline/
