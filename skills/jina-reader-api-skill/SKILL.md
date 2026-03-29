---
name: "Jina Reader API Skill"
description: "Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text."
category: "Research & Scraping"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jina-reader-api-skill/"
---
# Jina Reader API Skill

Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text.

## Overview

The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption.

The skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output.

For multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools.

The skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jina-reader-api-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jina-reader-api-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jina-reader-api-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jina-reader-api-skill -a codex
```

### OpenClaw

```bash
clawhub install jina-reader-api-skill
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
