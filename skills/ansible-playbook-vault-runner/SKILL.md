---
title: "Ansible Playbook Runner with Vault Secrets"
slug: "ansible-playbook-vault-runner"
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

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
