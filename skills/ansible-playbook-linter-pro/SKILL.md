---
name: "Ansible Playbook Linter Pro"
description: "Validates Ansible playbooks using ansible-lint with custom rule plugins and the Ansible Collections API. Checks for deprecated modules, missing handlers, insecure variable practices, and role dependency conflicts."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-linter-pro/"
tool_ecosystem:
  tool: "ansible"
  github_stars: 68377
  github_repo: "ansible/ansible"
  license: "GPL-3.0"
  maintained: true
---

# Ansible Playbook Linter Pro

Validates Ansible playbooks using ansible-lint with custom rule plugins and the Ansible Collections API. Checks for deprecated modules, missing handlers, insecure variable practices, and role dependency conflicts.

## Overview

The Ansible Playbook Linter Pro skill provides deep validation of Ansible playbooks, roles, and collections beyond what standard ansible-lint covers. It uses the ansible-lint framework with custom rule plugins and integrates with the Ansible Collections API (galaxy.ansible.com/api/v3) to verify module availability and deprecation status.

The skill extends ansible-lint with custom rules that detect common production issues: tasks without proper error handling (missing block/rescue structures), variables defined with no_log that might leak in debug mode, handlers that are notified but never defined, and role dependencies with version conflicts. Each custom rule follows the ansible-lint AnsibleLintRule base class pattern.

Collection and module validation queries the Ansible Galaxy API to check whether referenced collections are available, verify minimum version requirements, and flag modules marked as deprecated in favor of their replacements. The skill maintains a mapping of legacy module names to their fully qualified collection names (FQCN) and flags any bare module references.

Security-focused checks include scanning for hardcoded credentials in variable files, detecting unsafe uses of lookup plugins (pipe, url) without proper input validation, verifying that privilege escalation tasks use become with specific become_user rather than defaulting to root, and checking that sensitive file permissions are set correctly in file and template modules. Output includes both the ansible-lint SARIF format for CI integration and human-readable markdown reports.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-pro
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-pro -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-pro -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-linter-pro -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-linter-pro
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-linter-pro/
