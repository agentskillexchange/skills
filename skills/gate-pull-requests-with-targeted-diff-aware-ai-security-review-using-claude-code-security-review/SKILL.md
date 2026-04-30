---
title: "Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review"
description: "Run a Claude Code powered security review pass on trusted pull requests so suspicious auth, secret, injection, and unsafe logic changes surface before merge."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code-security-review"
author: "Anthropic"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "anthropics/claude-code-security-review"
  github_stars: 4304
---

# Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review

Run a Claude Code powered security review pass on trusted pull requests so suspicious auth, secret, injection, and unsafe logic changes surface before merge.

## Prerequisites

GitHub Actions, Claude API access, pull request workflows on trusted repositories

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add anthropics/claude-code-security-review to a GitHub Actions workflow that runs on trusted pull_request events, then configure the Claude API secret and any optional scan or filtering inputs.
```

## Documentation

- https://github.com/anthropics/claude-code-security-review

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review/)
