---
title: "Keep GitHub wiki pages synced with recently merged code changes"
description: "This entry turns GitHub Next’s Agentic Wiki Writer into a documentation-maintenance workflow. The agent watches for recent merges, reads the PAGES.md template, updates only the relevant wiki pages, and opens follow-up changes when the source structure itself needs adjustment."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/agentic-wiki-writer.md"
category: ["Templates &amp; Workflows"]
framework: ["Multi-Framework"]
---

# Keep GitHub wiki pages synced with recently merged code changes

This entry turns GitHub Next’s Agentic Wiki Writer into a documentation-maintenance workflow. The agent watches for recent merges, reads the PAGES.md template, updates only the relevant wiki pages, and opens follow-up changes when the source structure itself needs adjustment.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes/)
