---
name: "Ansible Playbook Template Generator"
description: "Generates Ansible playbook YAML with proper module usage, handler chains, and role structures using ansible-core built-in modules. Supports Jinja2 template rendering and vault-encrypted variable files."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-template-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ansible"  # from ase_tool_match
  github_stars: 68365  # from ase_github_stars (integer, not string)
  github_repo: "ansible/ansible"  # from ase_github_repo
  license: "GPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Ansible Playbook Template Generator

Generates Ansible playbook YAML with proper module usage, handler chains, and role structures using ansible-core built-in modules. Supports Jinja2 template rendering and vault-encrypted variable files.

## Overview

The Ansible Playbook Template Generator creates production-ready playbooks following Ansible best practices. It selects appropriate built-in modules from ansible-core including ansible.builtin.copy, ansible.builtin.template, ansible.builtin.service, and ansible.builtin.package with proper parameter specifications. The skill constructs handler chains with listen groups for cascading service restarts after configuration changes. Role structures follow the standard directory layout with defaults, vars, tasks, handlers, templates, and meta dependencies. Jinja2 templates use proper filter chains including default(), mandatory(), and custom filters with correct whitespace control using trim blocks and lstrip. Vault-encrypted variable files are managed with vault-id labels for multi-environment secret separation. The generator handles inventory patterns with group variables, host patterns using limit expressions, and dynamic inventory scripts for cloud provider integration. Includes proper error handling with block/rescue/always structures and async task patterns for long-running operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-generator -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-template-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-template-generator/
