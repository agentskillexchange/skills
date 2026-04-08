---
title: Ansible Playbook Debugger
description: 'The Ansible Playbook Debugger skill automates troubleshooting of Ansible
  playbook execution failures. It runs ansible-playbook with –check –diff flags for
  dry-run analysis, captures verbose output with -vvv for connection and module debugging,
  and parses structured JSON callback output using the json callback plugin. The skill
  integrates with ansible-lint for static analysis of playbooks, roles, and collections
  against best practices rules including command-instead-of-module, no-changed-when,
  and yaml[truthy]. It validates inventory files using ansible-inventory –graph and
  checks variable precedence through ansible-config dump. Diagnostic capabilities
  cover common failure modes: SSH connection issues diagnosed via ansible -m ping
  with transport debugging, privilege escalation failures analyzed through become
  configuration, module-specific errors in ansible.builtin.copy/template/service/package
  with parameter validation, and Jinja2 template rendering errors using ansible-playbook
  –syntax-check. Advanced features include execution strategy analysis (linear vs
  free vs mitogen), role dependency resolution via ansible-galaxy collection list,
  vault-encrypted variable debugging with ansible-vault view, and custom callback
  plugin development for structured error reporting. The skill also supports molecule
  test scenario analysis for role testing workflows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/ansible-playbook-debugger/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Ansible Playbook Debugger

The Ansible Playbook Debugger skill automates troubleshooting of Ansible playbook execution failures. It runs ansible-playbook with –check –diff flags for dry-run analysis, captures verbose output with -vvv for connection and module debugging, and parses structured JSON callback output using the json callback plugin. The skill integrates with ansible-lint for static analysis of playbooks, roles, and collections against best practices rules including command-instead-of-module, no-changed-when, and yaml[truthy]. It validates inventory files using ansible-inventory –graph and checks variable precedence through ansible-config dump. Diagnostic capabilities cover common failure modes: SSH connection issues diagnosed via ansible -m ping with transport debugging, privilege escalation failures analyzed through become configuration, module-specific errors in ansible.builtin.copy/template/service/package with parameter validation, and Jinja2 template rendering errors using ansible-playbook –syntax-check. Advanced features include execution strategy analysis (linear vs free vs mitogen), role dependency resolution via ansible-galaxy collection list, vault-encrypted variable debugging with ansible-vault view, and custom callback plugin development for structured error reporting. The skill also supports molecule test scenario analysis for role testing workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-debugger/)
