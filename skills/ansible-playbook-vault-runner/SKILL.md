---
name: "Ansible Playbook Runner with Vault Secrets"
slug: "ansible-playbook-vault-runner"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports --check mode for dry-run validation before live runs."
github_stars: 68348
verification: "listed"
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

Requirements and caveats from upstream:
- ad-hoc task execution, network automation, and multi-node orchestration. Ansible makes complex
- Allow module development in any dynamic language, not just Python.

Basic usage or getting-started notes:
- Power users and developers can run the devel branch, which has the latest
- in the Ansible community if you want to run the devel branch.

- Source: https://github.com/ansible/ansible
- Extracted from upstream docs: https://raw.githubusercontent.com/ansible/ansible/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
