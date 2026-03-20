---
name: Ansible Playbook Runner with Vault Secrets
description: Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: verified_metadata
rating: 4.6
reviews: 52
source: https://agentskillexchange.com/skill/ansible-playbook-vault-runner/
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs.

## Overview

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner
```

### OpenClaw

```bash
clawhub install ansible-playbook-vault-runner
```

### Claude Code

```bash
claude mcp add ansible-playbook-vault-runner
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/ansible-playbook-vault-runner/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.6/5 (52 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/ansible-playbook-vault-runner/)
