---
title: "Ansible Playbook Template Library"
description: "Generates and validates Ansible playbooks from infrastructure requirements. Uses ansible-lint for validation and queries Ansible Galaxy API for discovering certified roles and collections."
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
category:
  - "Templates &amp; Workflows"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-template-library/)
