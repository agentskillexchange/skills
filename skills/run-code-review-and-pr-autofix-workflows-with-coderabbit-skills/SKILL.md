---
title: "Run code review and PR autofix workflows with CodeRabbit Skills"
description: "Trigger CodeRabbit review passes from an agent and work unresolved PR feedback threads into guided or batch autofix loops."
verification: "listed"
source: "https://github.com/coderabbitai/skills"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "coderabbitai/skills"
  github_stars: 73
---

# Run code review and PR autofix workflows with CodeRabbit Skills

Use CodeRabbit Skills when the agent’s job is to run a CodeRabbit review over current changes or pull unresolved CodeRabbit PR comments into a fix-and-re-review workflow before merge. A user should invoke this instead of using CodeRabbit as a normal background product when they want the coding agent to actively launch the review, summarize findings, and optionally apply fixes from outstanding review threads. That boundary, agent-driven review and autofix execution around CodeRabbit CLI, keeps it from being just a generic code-review platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-code-review-and-pr-autofix-workflows-with-coderabbit-skills/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-code-review-and-pr-autofix-workflows-with-coderabbit-skills
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-code-review-and-pr-autofix-workflows-with-coderabbit-skills`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-code-review-and-pr-autofix-workflows-with-coderabbit-skills/)
