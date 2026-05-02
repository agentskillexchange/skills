---
title: "Search PDFs, Office files, ebooks, and archives with one query before manual review"
description: "Uses ripgrep-all to run one full-text search across mixed document and archive formats so an agent can find evidence without separately extracting every file type first. Best when a workflow has PDFs, Office documents, ebooks, media sidecars, or compressed bundles that need fast on-demand search."
verification: "security_reviewed"
source: "https://github.com/phiresky/ripgrep-all"
publisher_type: "User"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "phiresky/ripgrep-all"
  github_stars: 9573
---

# Search PDFs, Office files, ebooks, and archives with one query before manual review

Uses ripgrep-all to run one full-text search across mixed document and archive formats so an agent can find evidence without separately extracting every file type first. Best when a workflow has PDFs, Office documents, ebooks, media sidecars, or compressed bundles that need fast on-demand search.

## Prerequisites

ripgrep; optional adapters and dependencies such as pandoc, poppler, and ffmpeg.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install via Homebrew (`brew install rga`) or Cargo (`cargo install --locked ripgrep_all`).
```

## Documentation

- https://github.com/phiresky/ripgrep-all

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-pdfs-office-files-ebooks-and-archives-with-one-query-before-manual-review/)
