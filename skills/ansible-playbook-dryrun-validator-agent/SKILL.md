---
title: "Ansible Playbook Dry-Run Validator"
description: "The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with &#8211;check &#8211;diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution. The agent performs multi-layer validation including syntax checking via ansible-playbook &#8211;syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications. Advanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins."
source: "https://github.com/ansible/ansible"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry-Run Validator

The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with &#8211;check &#8211;diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution. The agent performs multi-layer validation including syntax checking via ansible-playbook &#8211;syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications. Advanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/)
