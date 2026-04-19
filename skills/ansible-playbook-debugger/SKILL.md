---
title: "Ansible Playbook Debugger"
description: "The Ansible Playbook Debugger skill automates troubleshooting of Ansible playbook execution failures. It runs ansible-playbook with &#8211;check &#8211;diff flags for dry-run analysis, captures verbose output with -vvv for connection and module debugging, and parses structured JSON callback output using the json callback plugin. The skill integrates with ansible-lint for static analysis of playbooks, roles, and collections against best practices rules including command-instead-of-module, no-changed-when, and yaml[truthy]. It validates inventory files using ansible-inventory &#8211;graph and checks variable precedence through ansible-config dump. Diagnostic capabilities cover common failure modes: SSH connection issues diagnosed via ansible -m ping with transport debugging, privilege escalation failures analyzed through become configuration, module-specific errors in ansible.builtin.copy/template/service/package with parameter validation, and Jinja2 template rendering errors using ansible-playbook &#8211;syntax-check. Advanced features include execution strategy analysis (linear vs free vs mitogen), role dependency resolution via ansible-galaxy collection list, vault-encrypted variable debugging with ansible-vault view, and custom callback plugin development for structured error reporting. The skill also supports molecule test scenario analysis for role testing workflows."
source: "https://github.com/ansible/ansible"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Debugger

The Ansible Playbook Debugger skill automates troubleshooting of Ansible playbook execution failures. It runs ansible-playbook with &#8211;check &#8211;diff flags for dry-run analysis, captures verbose output with -vvv for connection and module debugging, and parses structured JSON callback output using the json callback plugin. The skill integrates with ansible-lint for static analysis of playbooks, roles, and collections against best practices rules including command-instead-of-module, no-changed-when, and yaml[truthy]. It validates inventory files using ansible-inventory &#8211;graph and checks variable precedence through ansible-config dump. Diagnostic capabilities cover common failure modes: SSH connection issues diagnosed via ansible -m ping with transport debugging, privilege escalation failures analyzed through become configuration, module-specific errors in ansible.builtin.copy/template/service/package with parameter validation, and Jinja2 template rendering errors using ansible-playbook &#8211;syntax-check. Advanced features include execution strategy analysis (linear vs free vs mitogen), role dependency resolution via ansible-galaxy collection list, vault-encrypted variable debugging with ansible-vault view, and custom callback plugin development for structured error reporting. The skill also supports molecule test scenario analysis for role testing workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-debugger/)
