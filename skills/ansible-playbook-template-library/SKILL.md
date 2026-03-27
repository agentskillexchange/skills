---
name: "Ansible Playbook Template Library"
description: "Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections."
category: "Templates & Workflows"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-template-library/"
tool_ecosystem:
  tool: ansible
  github_stars: 68377
  npm_weekly_downloads: 9204385
  github_repo: ansible/ansible
  license: GPL-3.0
  maintained: true
---

# Ansible Playbook Template Library

Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections.

## Overview

This skill produces Ansible playbooks, roles, and inventories tailored to specific infrastructure automation needs. It queries the Ansible Galaxy API to find certified collections and community roles that match the requested automation tasks, then composes them into well-structured playbooks following Ansible best practices. The generator creates role directories with proper defaults, handlers, templates, and molecule test scenarios. It uses ansible-lint to validate generated playbooks against production rulesets, checking for deprecated modules, missing tags, and improper variable scoping. The skill supports dynamic inventory generation for AWS EC2, Azure VMs, and GCP instances using their respective inventory plugins. Vault-encrypted variable files are generated for sensitive data, and the skill produces accompanying ansible.cfg files with optimized settings for SSH pipelining, fact caching, and callback plugins.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-template-library -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-template-library
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-template-library/
