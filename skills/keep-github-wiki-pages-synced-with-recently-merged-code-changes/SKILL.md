---
name: "Keep GitHub wiki pages synced with recently merged code changes"
slug: "keep-github-wiki-pages-synced-with-recently-merged-code-changes"
description: "This entry turns GitHub Next's Agentic Wiki Writer into a documentation-maintenance workflow. The agent watches for recent merges, reads the PAGES.md template, updates only the relevant wiki pages, and opens follow-up changes when the source structure itself needs adjustment."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/agentic-wiki-writer.md"
author: "GitHub Next"
publisher_type: "Open Source Project"
category: "Templates & Workflows"
framework: "Multi-Framework"
---

# Keep GitHub wiki pages synced with recently merged code changes

This entry turns GitHub Next's Agentic Wiki Writer into a documentation-maintenance workflow. The agent watches for recent merges, reads the PAGES.md template, updates only the relevant wiki pages, and opens follow-up changes when the source structure itself needs adjustment.

## Prerequisites

GitHub CLI, the gh-aw extension, an enabled repository wiki, and a PAGES.md template or first-run template generation

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
gh extension install github/gh-aw && gh aw add-wizard githubnext/agentics/agentic-wiki-writer
```

## Documentation

- https://github.com/githubnext/agentics/blob/main/docs/agentic-wiki-writer.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes/)
