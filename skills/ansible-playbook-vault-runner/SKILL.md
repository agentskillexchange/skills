---
name: "Ansible Playbook Runner with Vault Secrets"
slug: "ansible-playbook-vault-runner"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs."
github_stars: 68348
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
author: "Ansible"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68348
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
