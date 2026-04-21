---
title: "Ansible Playbook Runner with Vault Secrets"
slug: "ansible-playbook-vault-runner"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs."
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

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
