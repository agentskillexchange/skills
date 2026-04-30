---
title: "Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents"
description: "Use issue labels as a lightweight dispatch layer that fans repository work out to Claude Code, Codex, or Aider workers and brings back PRs."
verification: "listed"
source: "https://github.com/hey-intent/patchwork-agents"
author: "hey-intent"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "hey-intent/patchwork-agents"
  github_stars: 0
---

# Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents

Use issue labels as a lightweight dispatch layer that fans repository work out to Claude Code, Codex, or Aider workers and brings back PRs.

## Prerequisites

GitHub App or webhook setup, Kubernetes or k3s environment, supported coding-agent credentials, repository access, Patchwork Agents deployment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Deploy the orchestrator and worker stack using the upstream Ansible or Kubernetes manifests, configure GitHub webhook and app credentials plus at least one supported agent provider, then apply the documented ai-pr label workflow to repository issues.
```

## Documentation

- https://github.com/hey-intent/patchwork-agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents/)
