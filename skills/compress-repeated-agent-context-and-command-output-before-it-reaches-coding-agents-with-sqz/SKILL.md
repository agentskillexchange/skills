---
title: "Compress repeated agent context and command output before it reaches coding agents with sqz"
description: "Reduces token burn by compressing command output and deduplicating repeated file reads before they are sent to Claude Code, Codex, Cursor, and related coding-agent tools."
verification: "security_reviewed"
source: "https://github.com/ojuschugh1/sqz"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ojuschugh1/sqz"
  github_stars: 165
---

# Compress repeated agent context and command output before it reaches coding agents with sqz

Use sqz when an agent is wasting tokens on large command output, repeated file reads, or verbose diffs across an iterative coding session. It is especially useful in repo-scale work where the same context gets pulled multiple times and you want the agent to keep working with less context bloat instead of manually pruning prompts.

This is skill-shaped because the workflow is narrow and operational: install the hook, let sqz intercept tool output, and shrink or deduplicate what the agent receives. It is not a generic LLM utility catalog entry or a broad productivity app listing. Invoke it when the job is specifically to reduce agent context volume while preserving usable command and file output.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/compress-repeated-agent-context-and-command-output-before-it-reaches-coding-agents-with-sqz/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/compress-repeated-agent-context-and-command-output-before-it-reaches-coding-agents-with-sqz
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/compress-repeated-agent-context-and-command-output-before-it-reaches-coding-agents-with-sqz`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compress-repeated-agent-context-and-command-output-before-it-reaches-coding-agents-with-sqz/)
