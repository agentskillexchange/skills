---
name: "Diffbot Article API to Markdown Pipeline"
description: "Turns Diffbot Article API responses into clean Markdown, frontmatter, and enrichment metadata for research and publishing workflows. It normalizes fields like title, author, tags, images, and dates, then prepares output for static sites, vector stores, or content review queues."
category: "Research & Scraping"
framework: "Claude Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/diffbot-article-api-markdown-pipeline-20260324/"
---

# Diffbot Article API to Markdown Pipeline

Turns Diffbot Article API responses into clean Markdown, frontmatter, and enrichment metadata for research and publishing workflows. It normalizes fields like title, author, tags, images, and dates, then prepares output for static sites, vector stores, or content review queues.

## Overview

This skill connects to the **Diffbot Article API** and transforms raw extraction output into a publishable or indexable Markdown package. Many teams can fetch a page and get JSON back, but they still need a reliable transformation layer that preserves title, author, publication date, lead image, section tags, and main body content while stripping navigation noise. The skill validates the API payload, resolves missing or conflicting fields, rewrites images and canonical URLs, and emits Markdown with YAML frontmatter or a JSON companion file. It is designed for article archives, media monitoring, newsroom research, and AI ingestion pipelines where consistency matters more than a one-off scrape.

Under the hood, the workflow accepts a URL list, calls the Diffbot endpoint with tokenized requests, inspects confidence-related fields, and maps the result into a normalized schema. It can split long bodies into chunks, add slug generation, classify content types, and write the output to disk, S3, or an object-store-compatible bucket. Downstream integrations include static site generators, LangChain or LlamaIndex document loaders, Elasticsearch, Meilisearch, Typesense, or a simple webhook that forwards processed articles into another service. The final output can include Markdown, JSON, CSV summaries, and failure logs for URLs that need manual review. That makes the skill useful both as an API connector and as a stable content transformation stage inside a larger ETL or editorial automation system.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-api-markdown-pipeline-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-api-markdown-pipeline-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-api-markdown-pipeline-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill diffbot-article-api-markdown-pipeline-20260324 -a codex
```

### OpenClaw

```bash
clawhub install diffbot-article-api-markdown-pipeline-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/diffbot-article-api-markdown-pipeline-20260324/
