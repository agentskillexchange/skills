---
title: "Ansible Playbook Dry-Run Analyzer"
description: "The Ansible Playbook Dry-Run Analyzer skill provides comprehensive analysis of Ansible playbook changes before they are applied to production infrastructure. It executes playbooks in check mode (–check –diff) and uses the ansible.posix.json callback plugin to capture structured output for detailed analysis.\nThe analyzer parses task results to categorize changes by type: file modifications, package installations, service restarts, user/group changes, and configuration template updates. For each changed task, it extracts the diff output showing exactly what would change, making it easy to review infrastructure modifications before applying them.\nIdempotency analysis identifies tasks that report changes on every run, indicating potential idempotency issues. Common problems detected include shell/command tasks without creates/removes conditions, template tasks with dynamic timestamps, and handlers that trigger unnecessarily. The skill recommends fixes for each idempotency violation.\nThe change impact report includes a risk assessment based on the scope and type of changes: service restarts are flagged as medium risk, package upgrades as high risk, and file permission changes as low risk. It generates rollback playbooks for high-risk changes and integrates with approval workflows via webhook notifications. The analyzer supports inventory-specific analysis, comparing dry-run results across staging and production environments."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Dry-Run Analyzer

The Ansible Playbook Dry-Run Analyzer skill provides comprehensive analysis of Ansible playbook changes before they are applied to production infrastructure. It executes playbooks in check mode (–check –diff) and uses the ansible.posix.json callback plugin to capture structured output for detailed analysis.
The analyzer parses task results to categorize changes by type: file modifications, package installations, service restarts, user/group changes, and configuration template updates. For each changed task, it extracts the diff output showing exactly what would change, making it easy to review infrastructure modifications before applying them.
Idempotency analysis identifies tasks that report changes on every run, indicating potential idempotency issues. Common problems detected include shell/command tasks without creates/removes conditions, template tasks with dynamic timestamps, and handlers that trigger unnecessarily. The skill recommends fixes for each idempotency violation.
The change impact report includes a risk assessment based on the scope and type of changes: service restarts are flagged as medium risk, package upgrades as high risk, and file permission changes as low risk. It generates rollback playbooks for high-risk changes and integrates with approval workflows via webhook notifications. The analyzer supports inventory-specific analysis, comparing dry-run results across staging and production environments.

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
