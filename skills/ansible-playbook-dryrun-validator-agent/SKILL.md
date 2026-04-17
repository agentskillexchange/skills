---
title: "Ansible Playbook Dry-Run Validator"
description: "The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with –check –diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution.\nThe agent performs multi-layer validation including syntax checking via ansible-playbook –syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications.\nAdvanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry-Run Validator

The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with –check –diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution.
The agent performs multi-layer validation including syntax checking via ansible-playbook –syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications.
Advanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-dryrun-validator-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-playbook-dryrun-validator-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/)
