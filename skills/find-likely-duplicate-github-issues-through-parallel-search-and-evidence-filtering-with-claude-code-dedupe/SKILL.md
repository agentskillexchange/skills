---
title: "Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe"
description: "Use Claude Code dedupe to summarize an issue, run several GitHub duplicate searches in parallel, filter false positives, and post only well-supported possible-duplicate links."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code/blob/main/.claude/commands/dedupe.md"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code"
  github_stars: 116829
  npm_package: "@anthropic-ai/claude-code"
  npm_weekly_downloads: 49934290
---

# Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe

This entry is built from Anthropic’s dedupe command for Claude Code. The agent workflow is explicit: skip closed or non-actionable issues, summarize the target issue, launch multiple search passes with different query strategies, filter weak matches, and only then post up to three likely duplicates. That makes the operator job concrete and repeatable rather than a generic GitHub utility card. Invoke this when a repository is large enough that duplicate reports waste maintainer time and quick keyword searches miss the real prior thread. The scope boundary is tight: this skill is only for evidence-backed duplicate hunting and duplicate-link posting. It is not a general issue triage suite, GitHub platform listing, or broad repository automation package.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe/)
