---
title: "Ansible Playbook Linter Pro"
description: "The Ansible Playbook Linter Pro skill provides deep validation of Ansible playbooks, roles, and collections beyond what standard ansible-lint covers. It uses the ansible-lint framework with custom rule plugins and integrates with the Ansible Collections API (galaxy.ansible.com/api/v3) to verify module availability and deprecation status.\nThe skill extends ansible-lint with custom rules that detect common production issues: tasks without proper error handling (missing block/rescue structures), variables defined with no_log that might leak in debug mode, handlers that are notified but never defined, and role dependencies with version conflicts. Each custom rule follows the ansible-lint AnsibleLintRule base class pattern.\nCollection and module validation queries the Ansible Galaxy API to check whether referenced collections are available, verify minimum version requirements, and flag modules marked as deprecated in favor of their replacements. The skill maintains a mapping of legacy module names to their fully qualified collection names (FQCN) and flags any bare module references.\nSecurity-focused checks include scanning for hardcoded credentials in variable files, detecting unsafe uses of lookup plugins (pipe, url) without proper input validation, verifying that privilege escalation tasks use become with specific become_user rather than defaulting to root, and checking that sensitive file permissions are set correctly in file and template modules. Output includes both the ansible-lint SARIF format for CI integration and human-readable markdown reports."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Linter Pro

The Ansible Playbook Linter Pro skill provides deep validation of Ansible playbooks, roles, and collections beyond what standard ansible-lint covers. It uses the ansible-lint framework with custom rule plugins and integrates with the Ansible Collections API (galaxy.ansible.com/api/v3) to verify module availability and deprecation status.
The skill extends ansible-lint with custom rules that detect common production issues: tasks without proper error handling (missing block/rescue structures), variables defined with no_log that might leak in debug mode, handlers that are notified but never defined, and role dependencies with version conflicts. Each custom rule follows the ansible-lint AnsibleLintRule base class pattern.
Collection and module validation queries the Ansible Galaxy API to check whether referenced collections are available, verify minimum version requirements, and flag modules marked as deprecated in favor of their replacements. The skill maintains a mapping of legacy module names to their fully qualified collection names (FQCN) and flags any bare module references.
Security-focused checks include scanning for hardcoded credentials in variable files, detecting unsafe uses of lookup plugins (pipe, url) without proper input validation, verifying that privilege escalation tasks use become with specific become_user rather than defaulting to root, and checking that sensitive file permissions are set correctly in file and template modules. Output includes both the ansible-lint SARIF format for CI integration and human-readable markdown reports.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-linter-pro
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-playbook-linter-pro` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-linter-pro/)
