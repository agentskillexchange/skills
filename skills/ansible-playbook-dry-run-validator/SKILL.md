---
title: "Ansible Playbook Dry Run Validator"
description: "Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections."
slug: "ansible-playbook-dry-run-validator"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/"
listed: true
---

# Ansible Playbook Dry Run Validator

Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections.

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
clawhub install ansible-playbook-dry-run-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Ansible Playbook Dry Run Validator skill combines ansible-lint static analysis with the Ansible Galaxy API (GET /api/v3/plugin/ansible/content/published/collections/index/) to validate playbook correctness before execution. It runs playbooks in check mode (–check –diff) against inventory to simulate changes without applying them. Role dependency resolution queries the Galaxy API to verify collection version compatibility and detect yanked versions. The skill maps deprecated module usage by parsing the Ansible changelog API and module documentation metadata to identify removed or redirected modules. Variable precedence analysis traces variable values through all 22 Ansible precedence levels to detect unintended overrides. Jinja2 template validation catches undefined variables, incorrect filter usage, and type mismatches before runtime. The skill generates compatibility matrices showing which Ansible core versions support the collections and modules used in the playbook. Integration test scaffolding uses Molecule configuration templates for automated playbook verification.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/)
