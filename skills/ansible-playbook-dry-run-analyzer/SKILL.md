---
title: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ansible-playbook-dry-run-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ansible-playbook-dry-run-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/)
