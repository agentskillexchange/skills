---
name: "Ansible Playbook Dry Run Validator"
description: "Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/"
---
# Ansible Playbook Dry Run Validator

Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections.

The Ansible Playbook Dry Run Validator skill combines ansible-lint static analysis with the Ansible Galaxy API (GET /api/v3/plugin/ansible/content/published/collections/index/) to validate playbook correctness before execution. It runs playbooks in check mode (–check –diff) against inventory to simulate changes without applying them. Role dependency resolution queries the Galaxy API to verify collection version compatibility and detect yanked versions. The skill maps deprecated module usage by parsing the Ansible changelog API and module documentation metadata to identify removed or redirected modules. Variable precedence analysis traces variable values through all 22 Ansible precedence levels to detect unintended overrides. Jinja2 template validation catches undefined variables, incorrect filter usage, and type mismatches before runtime. The skill generates compatibility matrices showing which Ansible core versions support the collections and modules used in the playbook. Integration test scaffolding uses Molecule configuration templates for automated playbook verification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-validator -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-dry-run-validator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/)
