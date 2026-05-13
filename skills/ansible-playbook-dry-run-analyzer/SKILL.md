---
title: "Ansible Playbook Dry-Run Analyzer"
slug: "ansible-playbook-dry-run-analyzer"
description: "Executes ansible-playbook --check --diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
github_stars: 68364
verification: "security_reviewed"
source: "https://github.com/ansible/ansible"
category: "Runbooks & Diagnostics"
framework: "Gemini"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook --check --diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/)
