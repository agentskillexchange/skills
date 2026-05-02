---
title: "Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents"
description: "Use issue labels as a lightweight dispatch layer that fans repository work out to Claude Code, Codex, or Aider workers and brings back PRs."
verification: "listed"
source: "https://github.com/hey-intent/patchwork-agents"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hey-intent/patchwork-agents"
---

# Dispatch coding agents from GitHub issue labels and return pull requests with Patchwork Agents

Use Patchwork Agents when the workflow is issue-label driven coding-agent dispatch, not ordinary GitHub issue triage or a generic Kubernetes platform. The job is specific: watch for ai-pr labels on issues, start the mapped worker, let it clone and solve the task, then push the result back as a pull request. That scope boundary, label-triggered issue-to-PR automation across supported coding agents, keeps this skill-shaped instead of collapsing into a plain orchestrator or product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dispatch-coding-agents-from-github-issue-labels-and-return-pull-requests-with-patchwork-agents/)
