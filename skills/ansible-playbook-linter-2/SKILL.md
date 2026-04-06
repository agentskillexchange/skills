---
name: Ansible Playbook Linter
description: Validates Ansible playbooks and roles using ansible-lint and yamllint
  APIs. Enforces best practices for idempotency, variable naming, and handler usage
  with custom rule profiles.
category: "Templates &amp; Workflows"
framework: Custom Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-linter-2/"
---
# Ansible Playbook Linter

Validates Ansible playbooks and roles using ansible-lint and yamllint APIs. Enforces best practices for idempotency, variable naming, and handler usage with custom rule profiles.

The Ansible Playbook Linter provides comprehensive validation of Ansible playbooks, roles, and collections against best practices and organizational standards. It wraps ansible-lint with custom rule profiles that enforce idempotency patterns, proper variable naming conventions (snake_case with role prefixes), handler usage, and task naming requirements. The tool runs yamllint as a preprocessing step to catch YAML syntax issues before semantic analysis. It validates Jinja2 template expressions within playbooks using jinja2-lint, catching undefined variables, filter misuse, and template syntax errors. For role validation, it checks meta/main.yml completeness, verifies all handlers referenced in tasks exist, and ensures defaults/main.yml documents all variables with comments. The linter integrates with molecule test scenarios to verify that playbooks are actually idempotent by checking for changed status on second runs. It supports custom rule authoring using Python rule classes and provides fix suggestions with auto-remediation for common issues like using shell instead of command, missing become declarations, and bare variables in when clauses.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-2 -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-linter-2
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-2/)
