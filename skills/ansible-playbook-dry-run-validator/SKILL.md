---
title: "Ansible Playbook Dry Run Validator"
description: "Validates Ansible playbooks using ansible-lint and the Ansible Galaxy API. Performs check-mode dry runs, validates role dependencies, and detects deprecated module usage across collections."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry Run Validator

The Ansible Playbook Dry Run Validator skill combines ansible-lint static analysis with the Ansible Galaxy API (GET /api/v3/plugin/ansible/content/published/collections/index/) to validate playbook correctness before execution. It runs playbooks in check mode (–check –diff) against inventory to simulate changes without applying them. Role dependency resolution queries the Galaxy API to verify collection version compatibility and detect yanked versions. The skill maps deprecated module usage by parsing the Ansible changelog API and module documentation metadata to identify removed or redirected modules. Variable precedence analysis traces variable values through all 22 Ansible precedence levels to detect unintended overrides. Jinja2 template validation catches undefined variables, incorrect filter usage, and type mismatches before runtime. The skill generates compatibility matrices showing which Ansible core versions support the collections and modules used in the playbook. Integration test scaffolding uses Molecule configuration templates for automated playbook verification.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-validator/)
