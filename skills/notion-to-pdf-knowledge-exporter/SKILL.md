---
name: "Notion to PDF Knowledge Exporter"
slug: "notion-to-pdf-knowledge-exporter"
description: "Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion."
github_stars: 5582
verification: "listed"
source: "https://github.com/makenotion/notion-sdk-js"
category: "Templates & Workflows"
framework: "Codex"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion to PDF Knowledge Exporter

Queries Notion databases and pages via the Notion API v1, then renders content blocks into PDF via WeasyPrint. Extracts text, tables, and inline images and preserves heading hierarchy. Generates per-section embeddings with OpenAI text-embedding-3-small for RAG ingestion.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @notionhq/client
- Make a request to any Notion API endpoint.

Requirements and caveats from upstream:
- const { Client } = require("@notionhq/client")
- const { Client, APIErrorCode } = require("@notionhq/client")
- const { Client, LogLevel } = require("@notionhq/client")

Basic usage or getting-started notes:
- bash
- [![Open Val Town Template](https://stevekrouse-badge.web.val.run/?3)](https://www.val.town/v/charmaine/NotionJsSDK)
- [!NOTE]

- Source: https://github.com/makenotion/notion-sdk-js
- Extracted from upstream docs: https://raw.githubusercontent.com/makenotion/notion-sdk-js/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-to-pdf-knowledge-exporter/)
