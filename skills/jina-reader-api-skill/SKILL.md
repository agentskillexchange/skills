---
name: "Jina Reader API Skill"
slug: "jina-reader-api-skill"
description: "Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text."
verification: "listed"
source: "https://jina.ai/reader/"
category: "Research & Scraping"
framework: "Gemini"
---

# Jina Reader API Skill

Extracts clean markdown content from any URL using the Jina Reader API (r.jina.ai). Handles JavaScript-rendered pages, PDF extraction, and multi-page crawling with depth control. Returns structured LLM-ready text.

## Installation

Requirements and caveats from upstream:
- Override the browser User-Agent string. Useful for accessing sites that require specific browsers or block crawlers.
- Type a question that requires latest information or world knowledge.
- Embedding API https://api.jina.ai/v1/embeddings Convert text/images to fixed-length vectors block 100 RPM & 100,000 TPM 500 RPM & 2,000,000 TPM trending_up 5,000 RPM & 50,000,000 TPM ssid_chart depends on the input size

Basic usage or getting-started notes:
- Run Jina models natively inside Elasticsearch.
- code Usage
- Only extract content matching these CSS selectors. Example: article, .main-content, #post-body

- Source: https://jina.ai/reader/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jina-reader-api-skill/)
