---
name: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook -check -diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
---

# Ansible Playbook Dry-Run Analyzer

The Ansible Playbook Dry-Run Analyzer skill provides comprehensive analysis of Ansible playbook changes before they are applied to production infrastructure. It executes playbooks in check mode (-check -diff) and uses the ansible.posix.json callback plugin to capture structured output for detailed analysis.
The analyzer parses task results to categorize changes by type: file modifications, package installations, service restarts, user/group changes, and configuration template updates. For each changed task, it extracts the diff output showing exactly what would change, making it easy to review infrastructure modifications before applying them.
Idempotency analysis identifies tasks that report changes on every run, indicating potential idempotency issues. Common problems detected include shell/command tasks without creates/removes conditions, template tasks with dynamic timestamps, and handlers that trigger unnecessarily. The skill recommends fixes for each idempotency violation.
The change impact report includes a risk assessment based on the scope and type of changes: service restarts are flagged as medium risk, package upgrades as high risk, and file permission changes as low risk. It generates rollback playbooks for high-risk changes and integrates with approval workflows via webhook notifications. The analyzer supports inventory-specific analysis, comparing dry-run results across staging and production environments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/)
