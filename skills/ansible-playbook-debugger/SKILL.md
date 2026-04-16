---
title: "Ansible Playbook Debugger"
description: "Diagnoses Ansible playbook failures using ansible-playbook –check –diff mode, ansible-lint, and the Ansible callback plugin API. Parses task execution results and suggests fixes for common module errors in ansible.builtin and community collections."
verification: "security_reviewed"
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

# Ansible Playbook Debugger

The Ansible Playbook Debugger skill automates troubleshooting of Ansible playbook execution failures. It runs ansible-playbook with –check –diff flags for dry-run analysis, captures verbose output with -vvv for connection and module debugging, and parses structured JSON callback output using the json callback plugin.


The skill integrates with ansible-lint for static analysis of playbooks, roles, and collections against best practices rules including command-instead-of-module, no-changed-when, and yaml[truthy]. It validates inventory files using ansible-inventory –graph and checks variable precedence through ansible-config dump.


Diagnostic capabilities cover common failure modes: SSH connection issues diagnosed via ansible -m ping with transport debugging, privilege escalation failures analyzed through become configuration, module-specific errors in ansible.builtin.copy/template/service/package with parameter validation, and Jinja2 template rendering errors using ansible-playbook –syntax-check.


Advanced features include execution strategy analysis (linear vs free vs mitogen), role dependency resolution via ansible-galaxy collection list, vault-encrypted variable debugging with ansible-vault view, and custom callback plugin development for structured error reporting. The skill also supports molecule test scenario analysis for role testing workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-debugger/)
