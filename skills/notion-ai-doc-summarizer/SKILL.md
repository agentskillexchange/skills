---
title: "Notion AI Document Summarizer & Action Item Extractor"
slug: "notion-ai-doc-summarizer"
description: "Uses the Notion SDK and Notion AI's /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create."
verification: "security_reviewed"
source: "https://github.com/makenotion/notion-sdk-js"
category: "Calendar, Email & Productivity"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion AI Document Summarizer & Action Item Extractor

Uses the Notion SDK and Notion AI's /v1/pages and /v1/blocks/children endpoints to retrieve page content and invoke AI-powered summarization. Extracted action items are appended as a structured database entry via databases.query and pages.create.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-ai-doc-summarizer/)
