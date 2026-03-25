---
name: "Ansible Playbook Debugger"
description: "Diagnoses Ansible playbook failures using ansible-playbook –check –diff mode, ansible-lint, and the Ansible callback plugin API. Parses task execution results and suggests fixes for common module errors in ansible.builtin and community collections."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-debugger/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ansible"  # from ase_tool_match
  github_stars: 68377  # from ase_github_stars (integer, not string)
  github_repo: "ansible/ansible"  # from ase_github_repo
  license: "GPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Ansible Playbook Debugger

Diagnoses Ansible playbook failures using ansible-playbook –check –diff mode, ansible-lint, and the Ansible callback plugin API. Parses task execution results and suggests fixes for common module errors in ansible.builtin and community collections.

## Overview

The Ansible Playbook Debugger skill automates troubleshooting of Ansible playbook execution failures. It runs ansible-playbook with –check –diff flags for dry-run analysis, captures verbose output with -vvv for connection and module debugging, and parses structured JSON callback output using the json callback plugin.

The skill integrates with ansible-lint for static analysis of playbooks, roles, and collections against best practices rules including command-instead-of-module, no-changed-when, and yaml[truthy]. It validates inventory files using ansible-inventory –graph and checks variable precedence through ansible-config dump.

Diagnostic capabilities cover common failure modes: SSH connection issues diagnosed via ansible -m ping with transport debugging, privilege escalation failures analyzed through become configuration, module-specific errors in ansible.builtin.copy/template/service/package with parameter validation, and Jinja2 template rendering errors using ansible-playbook –syntax-check.

Advanced features include execution strategy analysis (linear vs free vs mitogen), role dependency resolution via ansible-galaxy collection list, vault-encrypted variable debugging with ansible-vault view, and custom callback plugin development for structured error reporting. The skill also supports molecule test scenario analysis for role testing workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-debugger -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-debugger/
