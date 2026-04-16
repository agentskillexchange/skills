---
title: "Jina Reader API Skill"
description: "Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/jina-reader-api-skill/"
category:
  - "Research &amp; Scraping"
framework:
  - "Gemini"
---

# Jina Reader API Skill

The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption.

The skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output.

For multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools.

The skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
