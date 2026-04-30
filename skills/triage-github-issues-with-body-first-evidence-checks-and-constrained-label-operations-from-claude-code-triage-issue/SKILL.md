---
title: "Triage GitHub issues with body-first evidence checks and constrained label operations from Claude Code triage-issue"
description: "Use Claude Code triage-issue to read a GitHub issue, verify it actually belongs to the product from body evidence first, check nearby duplicates, and apply only allowed labels without drifting into open-ended repo management."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code/blob/main/.claude/commands/triage-issue.md"
author: "Anthropic"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# Triage GitHub issues with body-first evidence checks and constrained label operations from Claude Code triage-issue

Use Claude Code triage-issue to read a GitHub issue, verify it actually belongs to the product from body evidence first, check nearby duplicates, and apply only allowed labels without drifting into open-ended repo management.

## Prerequisites

Claude Code, GitHub repository access, repository-provided gh wrapper/label scripts

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Claude Code from the official docs, then use the repository's triage-issue command file in a repo that exposes the expected GitHub wrapper scripts and label-edit script.
```

## Documentation

- https://code.claude.com/docs/en/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue/)
