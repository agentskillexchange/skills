---
title: "Ansible Playbook Template Library"
description: "Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections."
slug: "ansible-playbook-template-library"
category:
  - "Templates &amp; Workflows"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-playbook-template-library/"
listed: true
---

# Ansible Playbook Template Library

Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ansible-playbook-template-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill produces Ansible playbooks, roles, and inventories tailored to specific infrastructure automation needs. It queries the Ansible Galaxy API to find certified collections and community roles that match the requested automation tasks, then composes them into well-structured playbooks following Ansible best practices. The generator creates role directories with proper defaults, handlers, templates, and molecule test scenarios. It uses ansible-lint to validate generated playbooks against production rulesets, checking for deprecated modules, missing tags, and improper variable scoping. The skill supports dynamic inventory generation for AWS EC2, Azure VMs, and GCP instances using their respective inventory plugins. Vault-encrypted variable files are generated for sensitive data, and the skill produces accompanying ansible.cfg files with optimized settings for SSH pipelining, fact caching, and callback plugins.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-template-library/)
