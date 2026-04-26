---
title: "Lint Ansible playbooks and roles before automation breaks in prod with ansible-lint"
description: "Run ansible-lint against playbooks, roles, and collections so risky patterns and common mistakes are caught before automation is merged or executed."
verification: "listed"
source: "https://github.com/ansible/ansible-lint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ansible/ansible-lint"
  github_stars: 3856
---

# Lint Ansible playbooks and roles before automation breaks in prod with ansible-lint

This skill runs ansible-lint on Ansible content and helps agents interpret and fix the findings. Invoke it when you need a bounded pre-run or pre-merge review of playbooks, roles, or collections instead of manually scanning YAML or relying on a generic Ansible runner. The boundary is clear: the agent is performing a lint-and-remediate workflow for infrastructure code quality, not publishing ansible-lint as a generic tool listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/lint-ansible-playbooks-and-roles-before-automation-breaks-in-prod-with-ansible-lint/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-ansible-playbooks-and-roles-before-automation-breaks-in-prod-with-ansible-lint
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/lint-ansible-playbooks-and-roles-before-automation-breaks-in-prod-with-ansible-lint`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-ansible-playbooks-and-roles-before-automation-breaks-in-prod-with-ansible-lint/)
