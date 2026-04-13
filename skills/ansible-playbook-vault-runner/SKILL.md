---
name: "ansible-playbook-vault-runner"
title: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68348
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
