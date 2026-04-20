---
title: "Notion AI Document Summarizer & Action Item Extractor"
description: "Uses the Notion SDK and Notion AI's /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create."
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion AI Document Summarizer & Action Item Extractor

Uses the Notion SDK and Notion AI's /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/notion-ai-doc-summarizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/notion-ai-doc-summarizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/notion-ai-doc-summarizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-ai-doc-summarizer/)
