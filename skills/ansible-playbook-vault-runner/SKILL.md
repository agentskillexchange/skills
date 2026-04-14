---
title: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68348
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports &#8211;check mode for dry-run validation before live runs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
