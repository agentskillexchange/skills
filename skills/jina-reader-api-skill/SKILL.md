---
title: "Jina Reader API Skill"
description: "Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text."
verification: "security_reviewed"
source: "https://jina.ai/reader/"
category:
  - "Research & Scraping"
framework:
  - "Gemini"
---

# Jina Reader API Skill

The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption.

The skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output.

For multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools.

The skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/jina-reader-api-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jina-reader-api-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/jina-reader-api-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
