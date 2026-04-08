---
title: "Ansible Playbook Runner with Vault Secrets"
slug: "ansible-playbook-vault-runner"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports -check mode for dry-run validation before live runs."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-playbook-vault-runner/"
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports -check mode for dry-run validation before live runs.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
