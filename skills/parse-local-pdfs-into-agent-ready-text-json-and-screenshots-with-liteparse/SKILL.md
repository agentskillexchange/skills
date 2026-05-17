---
title: "Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse"
slug: "parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse"
description: "Run LiteParse locally to extract PDF text, spatial JSON, OCR-backed output, and page screenshots before sending documents into an agent workflow."
github_stars: 5136
verification: "listed"
source: "https://github.com/run-llama/liteparse"
author: "LlamaIndex"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "run-llama/liteparse"
  github_stars: 5136
  npm_package: "@llamaindex/liteparse"
  npm_weekly_downloads: 36959
---

# Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse

Run LiteParse locally to extract PDF text, spatial JSON, OCR-backed output, and page screenshots before sending documents into an agent workflow.

## Prerequisites

Node.js, npm or Homebrew, LiteParse CLI (`lit`), optional OCR server

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm i -g @llamaindex/liteparse` or `brew tap run-llama/liteparse && brew install llamaindex-liteparse`, then run `lit parse document.pdf --format json` or `lit screenshot document.pdf -o ./screenshots`.
```

## Documentation

- https://developers.llamaindex.ai/liteparse/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse/)
