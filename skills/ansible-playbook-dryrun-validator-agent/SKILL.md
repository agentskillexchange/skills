---
title: "Ansible Playbook Dry-Run Validator"
description: "Validates Ansible playbooks in check mode using ansible-playbook –check –diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs."
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
  license: "GPL-3.0"
---

# Ansible Playbook Dry-Run Validator

The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with –check –diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution.

The agent performs multi-layer validation including syntax checking via ansible-playbook –syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications.

Advanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/)
