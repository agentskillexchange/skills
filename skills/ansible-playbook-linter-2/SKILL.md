---
title: "Ansible Playbook Linter"
description: "Validates Ansible playbooks and roles using ansible-lint and yamllint APIs. Enforces best practices for idempotency, variable naming, and handler usage with custom rule profiles."
slug: "ansible-playbook-linter-2"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-playbook-linter-2/"
---

# Ansible Playbook Linter

Validates Ansible playbooks and roles using ansible-lint and yamllint APIs. Enforces best practices for idempotency, variable naming, and handler usage with custom rule profiles.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ansible-playbook-linter-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-2/)
