---
title: "Run multi-agent code review rounds with structured reviewer discourse before human approval"
description: "Use Open Code Review when an agent needs several reviewer personas to inspect a diff, debate findings, and synthesize review output before a human approves, posts, or acts on the review."
verification: "security_reviewed"
source: "https://github.com/spencermarx/open-code-review"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "spencermarx/open-code-review"
  github_stars: 131
  npm_package: "@open-code-review/cli"
  npm_weekly_downloads: 1089
---

# Run multi-agent code review rounds with structured reviewer discourse before human approval

Open Code Review gives an agent a narrow code-review workflow rather than a generic coding platform. It initializes a review project, analyzes a diff or requirements context, runs several reviewer agents in parallel, preserves their discourse, and produces structured findings plus a synthesized review that can be browsed in the dashboard or posted back to a pull request.

The scope stays tight: this is for multi-agent review rounds on code changes. It is not a generic IDE, not a broad AI coding assistant listing, and not a general CI platform card. Invoke it when the missing step is deeper review coverage and reviewer debate before human sign-off, not when the user simply wants another code editor or single-agent coding tool.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-multi-agent-code-review-rounds-with-structured-reviewer-discourse-before-human-approval/)
