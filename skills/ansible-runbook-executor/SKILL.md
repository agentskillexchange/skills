---
title: "Ansible Runbook Executor"
description: "Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
  license: "GPL-3.0"
---

# Ansible Runbook Executor

The Ansible Runbook Executor agent leverages the ansible-runner Python SDK to execute diagnostic and remediation playbooks on remote infrastructure. It parses YAML-based inventory files, resolves host groups, and manages vault-encrypted secrets for secure credential handling during execution.

Designed for incident response, the agent can run pre-defined runbooks for common scenarios: disk space cleanup, service restarts, log collection, certificate rotation, and DNS resolution checks. Each playbook execution produces structured JSON output with per-host task results, return codes, and stdout/stderr capture.

The agent streams real-time task output via ansible-runner event handlers, enabling live progress tracking during long-running operations. It supports check mode (dry-run) for validation before applying changes, and integrates with Ansible Galaxy for pulling community roles. Tags and limits can be applied dynamically to scope execution to specific hosts or task subsets.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-runbook-executor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-runbook-executor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-runbook-executor/)
