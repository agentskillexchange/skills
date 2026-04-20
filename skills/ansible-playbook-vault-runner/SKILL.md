---
title: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports -check mode for dry-run validation before live runs."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68348
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports -check mode for dry-run validation before live runs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ansible-playbook-vault-runner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-vault-runner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ansible-playbook-vault-runner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
