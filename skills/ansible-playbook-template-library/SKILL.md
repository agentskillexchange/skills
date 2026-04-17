---
title: "Ansible Playbook Template Library"
description: "Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Templates & Workflows"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
  license: "GPL-3.0"
---

# Ansible Playbook Template Library

This skill produces Ansible playbooks, roles, and inventories tailored to specific infrastructure automation needs. It queries the Ansible Galaxy API to find certified collections and community roles that match the requested automation tasks, then composes them into well-structured playbooks following Ansible best practices. The generator creates role directories with proper defaults, handlers, templates, and molecule test scenarios. It uses ansible-lint to validate generated playbooks against production rulesets, checking for deprecated modules, missing tags, and improper variable scoping. The skill supports dynamic inventory generation for AWS EC2, Azure VMs, and GCP instances using their respective inventory plugins. Vault-encrypted variable files are generated for sensitive data, and the skill produces accompanying ansible.cfg files with optimized settings for SSH pipelining, fact caching, and callback plugins.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-template-library
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-playbook-template-library` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-template-library/)
