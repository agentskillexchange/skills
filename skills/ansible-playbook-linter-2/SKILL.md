---
title: "Ansible Playbook Linter"
description: "Validates Ansible playbooks and roles using ansible-lint and yamllint APIs. Enforces best practices for idempotency, variable naming, and handler usage with custom rule profiles."
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Linter

The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ansible-playbook-linter-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-linter-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ansible-playbook-linter-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-2/)
