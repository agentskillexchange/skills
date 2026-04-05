---
name: "Ansible Playbook Dry-Run Validator"
description: "Validates Ansible playbooks in check mode using ansible-playbook –check –diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs."
category: "Runbooks &amp; Diagnostics"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/"
---
# Ansible Playbook Dry-Run Validator

Validates Ansible playbooks in check mode using ansible-playbook –check –diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dryrun-validator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dryrun-validator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dryrun-validator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dryrun-validator-agent -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-dryrun-validator-agent
```

## Details

The Ansible Playbook Dry-Run Validator ensures playbook safety by running comprehensive validation before production execution. It uses ansible-playbook with –check –diff flags for dry-run simulation and the Ansible Python API for programmatic playbook introspection and variable resolution.

The agent performs multi-layer validation including syntax checking via ansible-playbook –syntax-check, variable resolution verification against inventory and group_vars, role dependency validation, and conditional logic analysis for when/failed_when clauses. It detects common issues like undefined variables that only surface in specific host groups, non-idempotent tasks that would change state on every run, and missing handler notifications.

Advanced capabilities include generating change prediction reports showing exactly which hosts and tasks would be modified, validating Ansible Vault encrypted variables without decrypting them in logs, and testing playbook compatibility across multiple Ansible versions. The agent supports playbook collections, custom modules, and dynamic inventory sources including AWS EC2, Azure, and GCP inventory plugins.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/)
