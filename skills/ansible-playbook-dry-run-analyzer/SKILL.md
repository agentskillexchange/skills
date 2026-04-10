---
title: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
slug: "ansible-playbook-dry-run-analyzer"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/"
listed: true
---

# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

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
clawhub install ansible-playbook-dry-run-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Ansible Playbook Dry-Run Analyzer skill provides comprehensive analysis of Ansible playbook changes before they are applied to production infrastructure. It executes playbooks in check mode (–check –diff) and uses the ansible.posix.json callback plugin to capture structured output for detailed analysis.
The analyzer parses task results to categorize changes by type: file modifications, package installations, service restarts, user/group changes, and configuration template updates. For each changed task, it extracts the diff output showing exactly what would change, making it easy to review infrastructure modifications before applying them.
Idempotency analysis identifies tasks that report changes on every run, indicating potential idempotency issues. Common problems detected include shell/command tasks without creates/removes conditions, template tasks with dynamic timestamps, and handlers that trigger unnecessarily. The skill recommends fixes for each idempotency violation.
The change impact report includes a risk assessment based on the scope and type of changes: service restarts are flagged as medium risk, package upgrades as high risk, and file permission changes as low risk. It generates rollback playbooks for high-risk changes and integrates with approval workflows via webhook notifications. The analyzer supports inventory-specific analysis, comparing dry-run results across staging and production environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/)
