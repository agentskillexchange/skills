---
title: Jina Reader API Skill
description: The Jina Reader API Skill provides Claude with reliable web content extraction
  through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina
  Reader renders JavaScript, strips navigation chrome, and returns clean markdown
  suitable for LLM consumption. The skill prepends the target URL to the Jina endpoint
  (https://r.jina.ai/[url]) and parses the returned markdown content. It supports
  header-based configuration for controlling output format, including setting x-respond-with
  to specify markdown, text, or HTML output. For multi-page research, the skill implements
  depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related
  pages before extracting each one. PDF URLs are automatically handled — Jina extracts
  text from PDF documents without requiring local PDF processing tools. The skill
  includes content length estimation to warn about token budget impacts before processing
  large pages. It caches results for repeated access to the same URL within a session.
  Particularly useful for research workflows, documentation ingestion, and competitive
  analysis where clean text extraction from diverse web sources is essential.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jina-reader-api-skill/
category:
- Research &amp; Scraping
framework:
- Gemini
---

# Jina Reader API Skill

The Jina Reader API Skill provides Claude with reliable web content extraction through Jina’s hosted reader service at r.jina.ai. Unlike simple HTTP fetches, Jina Reader renders JavaScript, strips navigation chrome, and returns clean markdown suitable for LLM consumption. The skill prepends the target URL to the Jina endpoint (https://r.jina.ai/[url]) and parses the returned markdown content. It supports header-based configuration for controlling output format, including setting x-respond-with to specify markdown, text, or HTML output. For multi-page research, the skill implements depth-controlled crawling using Jina’s search endpoint (s.jina.ai) to discover related pages before extracting each one. PDF URLs are automatically handled — Jina extracts text from PDF documents without requiring local PDF processing tools. The skill includes content length estimation to warn about token budget impacts before processing large pages. It caches results for repeated access to the same URL within a session. Particularly useful for research workflows, documentation ingestion, and competitive analysis where clean text extraction from diverse web sources is essential.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
