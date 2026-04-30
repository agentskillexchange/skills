---
title: "Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe"
description: "Use Claude Code dedupe to summarize an issue, run several GitHub duplicate searches in parallel, filter false positives, and post only well-supported possible-duplicate links."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code/blob/main/.claude/commands/dedupe.md"
author: "Anthropic"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe

Use Claude Code dedupe to summarize an issue, run several GitHub duplicate searches in parallel, filter false positives, and post only well-supported possible-duplicate links.

## Prerequisites

Claude Code, GitHub repository access, repository-provided gh wrapper/comment scripts

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Claude Code from the official docs, then use the repository's dedupe command file in a repo that provides the expected GitHub wrapper and duplicate-comment scripts.
```

## Documentation

- https://code.claude.com/docs/en/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe/)
