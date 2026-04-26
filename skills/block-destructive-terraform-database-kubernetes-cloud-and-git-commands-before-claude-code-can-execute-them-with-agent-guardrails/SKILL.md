---
title: "Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails"
description: "Add hard pre-execution guardrails to Claude Code so destructive shell commands are blocked before an agent can run them."
verification: "listed"
source: "https://github.com/roboticforce/agent-guardrails"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "roboticforce/agent-guardrails"
  github_stars: 2
---

# Block destructive Terraform, database, Kubernetes, cloud, and Git commands before Claude Code can execute them with Agent Guardrails

Use Agent Guardrails when you want Claude Code to help with infrastructure or repository work but you need hard blocks on destructive commands first. Invoke this instead of using Claude Code normally when the missing step is policy enforcement on shell actions such as `terraform destroy`, `DROP DATABASE`, dangerous `kubectl delete`, or force pushes. The scope boundary is narrow and skill-shaped: pre-tool command interception and blocking for Claude Code, not a generic security platform or plain config bundle listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-destructive-terraform-database-kubernetes-cloud-and-git-commands-before-claude-code-can-execute-them-with-agent-guardrails/)
