---
title: "Triage GitHub issues with body-first evidence checks and constrained label operations from Claude Code triage-issue"
description: "Use Claude Code triage-issue to read a GitHub issue, verify it actually belongs to the product from body evidence first, check nearby duplicates, and apply only allowed labels without drifting into open-ended repo management."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code/blob/main/.claude/commands/triage-issue.md"
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

# Triage GitHub issues with body-first evidence checks and constrained label operations from Claude Code triage-issue

This entry is built from Anthropic’s triage-issue command for Claude Code. The agent job is narrow and operator-facing: inspect a newly filed GitHub issue, decide whether it is genuinely about Claude Code based on issue-body evidence, review the conversation, search for nearby duplicates, and then add or remove only labels that already exist in the repository. The workflow is intentionally constrained to label operations rather than free-form issue handling.

Invoke this instead of using GitHub normally when maintainers need consistent first-pass issue intake with explicit evidence rules and low-overreach guardrails. The scope boundary keeps it skill-shaped: it is not a listing for GitHub, the gh CLI, or Claude Code as a whole. It is specifically the evidence-first issue qualification and labeling loop for new or ambiguous issues.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue/)
