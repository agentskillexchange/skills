---
title: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs."
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68348
---
# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs.

## Installation

You can install this skill in a few common ways:

1. Browse and install from Agent Skill Exchange in the UI if your client supports it.
2. Install from a local skill folder by copying it into your skills directory.
3. Add it as a git submodule or vendor it into your shared skills repo.
4. Fetch it with your preferred skill or package workflow if the upstream project publishes one.
5. Follow the upstream project documentation for manual setup and dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
