---
title: "Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues"
description: "Use Claude Code as a bounded GitHub Actions worker for PR reviews, issue follow-up, and repository automation that stays inside normal workflow triggers and runner policy."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code-action"
author: "Anthropic"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-action"
  github_stars: 7136
---

# Run Claude Code inside GitHub Actions for scoped fix, review, and triage loops on pull requests and issues

Use Claude Code as a bounded GitHub Actions worker for PR reviews, issue follow-up, and repository automation that stays inside normal workflow triggers and runner policy.

## Prerequisites

GitHub Actions, Claude Code, Anthropic API key or supported cloud provider credentials

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add anthropics/claude-code-action to a GitHub Actions workflow, configure the triggering event, then provide the required Claude authentication secret and any workflow-specific prompts or claude_args inputs.
```

## Documentation

- https://github.com/anthropics/claude-code-action

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-code-inside-github-actions-for-scoped-fix-review-and-triage-loops-on-pull-requests-and-issues/)
