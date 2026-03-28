---
name: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/ansible/ansible"
tool_ecosystem:
  tool: ansible
  github_stars: 68377
  github_repo: ansible/ansible
  license: GPL-3.0
  maintained: true
---

# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

## Overview

The Ansible Playbook Dry-Run Analyzer skill provides comprehensive analysis of Ansible playbook changes before they are applied to production infrastructure. It executes playbooks in check mode (–check –diff) and uses the ansible.posix.json callback plugin to capture structured output for detailed analysis.

The analyzer parses task results to categorize changes by type: file modifications, package installations, service restarts, user/group changes, and configuration template updates. For each changed task, it extracts the diff output showing exactly what would change, making it easy to review infrastructure modifications before applying them.

Idempotency analysis identifies tasks that report changes on every run, indicating potential idempotency issues. Common problems detected include shell/command tasks without creates/removes conditions, template tasks with dynamic timestamps, and handlers that trigger unnecessarily. The skill recommends fixes for each idempotency violation.

The change impact report includes a risk assessment based on the scope and type of changes: service restarts are flagged as medium risk, package upgrades as high risk, and file permission changes as low risk. It generates rollback playbooks for high-risk changes and integrates with approval workflows via webhook notifications. The analyzer supports inventory-specific analysis, comparing dry-run results across staging and production environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-analyzer -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-dry-run-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/
