---
name: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-vault-runner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ansible"  # from ase_tool_match
  github_stars: 68365  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "ansible/ansible"  # from ase_github_repo
  license: "GPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Overview

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-vault-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-vault-runner/
