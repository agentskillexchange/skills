---
title: "Jina Reader API Skill"
description: "The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption.\nThe skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output.\nFor multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools.\nThe skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/jina-reader-api-skill/"
framework:
  - "Gemini"
---

# Jina Reader API Skill

The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption.
The skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output.
For multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools.
The skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jina-reader-api-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jina-reader-api-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
