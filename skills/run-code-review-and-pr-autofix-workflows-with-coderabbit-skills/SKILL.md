---
title: "Run code review and PR autofix workflows with CodeRabbit Skills"
description: "Trigger CodeRabbit review passes from an agent and work unresolved PR feedback threads into guided or batch autofix loops."
verification: "security_reviewed"
source: "https://github.com/coderabbitai/skills"
author: "CodeRabbit"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "coderabbitai/skills"
  github_stars: 73
---

# Run code review and PR autofix workflows with CodeRabbit Skills

Trigger CodeRabbit review passes from an agent and work unresolved PR feedback threads into guided or batch autofix loops.

## Prerequisites

CodeRabbit CLI, authenticated CodeRabbit access, a Git repository with local changes or an open PR, and an agent that supports Agent Skills

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install and authenticate the CodeRabbit CLI, add the skills repo with npx skills add coderabbitai/skills, then invoke the documented review or autofix prompts from a supported coding agent inside the target repository.
```

## Documentation

- https://docs.coderabbit.ai/cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-code-review-and-pr-autofix-workflows-with-coderabbit-skills/)
