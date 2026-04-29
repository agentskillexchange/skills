---
title: "Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action"
description: "Use codex-action when an agent operator wants Codex to run inside GitHub Actions for PR review or scheduled repo work with explicit workflow permissions, prompts, and CI boundaries."
verification: "security_reviewed"
source: "https://github.com/openai/codex-action"
author: "OpenAI"
publisher_type: "company"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "openai/codex-action"
  github_stars: 927
---

# Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action

Use codex-action when an agent operator wants Codex to run inside GitHub Actions for PR review or scheduled repo work with explicit workflow permissions, prompts, and CI boundaries.

## Prerequisites

GitHub Actions, a repository workflow file, Codex Action, and the required provider API secret configured in GitHub.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add openai/codex-action to a GitHub Actions workflow, configure the needed API secret in the repository or organization, choose the prompt source and sandbox mode for the job, then wire the action output into PR comments, checks, or other CI follow-up steps.
```

## Documentation

- https://github.com/openai/codex-action#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action/)
