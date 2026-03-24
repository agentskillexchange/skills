---
name: "Notion AI Document Summarizer & Action Item Extractor"
description: "Uses the Notion SDK and Notion AI’s /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/notion-ai-doc-summarizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "notion"  # from ase_tool_match
  github_stars: 5562  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1084242  # from ase_npm_downloads
  github_repo: "makenotion/notion-sdk-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Notion AI Document Summarizer & Action Item Extractor

Uses the Notion SDK and Notion AI’s /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create.

## Overview

Uses the Notion SDK and Notion AI’s /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-ai-doc-summarizer -a codex
```

### OpenClaw

```bash
clawhub install notion-ai-doc-summarizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/notion-ai-doc-summarizer/
