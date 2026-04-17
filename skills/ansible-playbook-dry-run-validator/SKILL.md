---
title: "Ansible Playbook Dry Run Validator"
description: "Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
  license: "GPL-3.0"
---

# Ansible Playbook Dry Run Validator

The Ansible Playbook Dry Run Validator skill combines ansible-lint static analysis with the Ansible Galaxy API (GET /api/v3/plugin/ansible/content/published/collections/index/) to validate playbook correctness before execution. It runs playbooks in check mode (–check –diff) against inventory to simulate changes without applying them. Role dependency resolution queries the Galaxy API to verify collection version compatibility and detect yanked versions. The skill maps deprecated module usage by parsing the Ansible changelog API and module documentation metadata to identify removed or redirected modules. Variable precedence analysis traces variable values through all 22 Ansible precedence levels to detect unintended overrides. Jinja2 template validation catches undefined variables, incorrect filter usage, and type mismatches before runtime. The skill generates compatibility matrices showing which Ansible core versions support the collections and modules used in the playbook. Integration test scaffolding uses Molecule configuration templates for automated playbook verification.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-dry-run-validator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-playbook-dry-run-validator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/)
