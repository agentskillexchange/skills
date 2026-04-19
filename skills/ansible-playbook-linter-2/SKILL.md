---
title: "Ansible Playbook Linter"
description: "The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses."
source: "https://github.com/ansible/ansible"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Linter

The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-2/)
