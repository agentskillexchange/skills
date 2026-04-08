---
title: Ansible Playbook Linter
description: The Ansible Playbook Linter provides comprehensive validation of Ansible
  playbooks, roles, and collections against best practices and organizational standards.
  It wraps ansible-lint with custom rule profiles that enforce idempotency patterns,
  proper variable naming conventions (snake_case with role prefixes), handler usage,
  and task naming requirements. The tool runs yamllint as a preprocessing step to
  catch YAML syntax issues before semantic analysis. It validates Jinja2 template
  expressions within playbooks using jinja2-lint, catching undefined variables, filter
  misuse, and template syntax errors. For role validation, it checks meta/main.yml
  completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml
  documents all variables with comments. The linter integrates with molecule test
  scenarios to verify that playbooks are actually idempotent by checking for changed
  status on second runs. It supports custom rule authoring using Python rule classes
  and provides fix suggestions with auto-remediation for common issues like using
  shell instead of command, missing become declarations, and bare variables in when
  clauses.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ansible-playbook-linter-2/
category:
- Templates &amp; Workflows
framework:
- Custom Agents
---

# Ansible Playbook Linter

The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-2/)
