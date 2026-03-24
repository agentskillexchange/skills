---
name: "Ansible Playbook Dry-Run Validator"
description: "Validates Ansible playbooks in check mode using ansible-playbook --check --diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 4.9
reviews: 79
creator: "Ben Taylor"
creator_handle: "@bentaylor"
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/"
---

# Ansible Playbook Dry-Run Validator

Validates Ansible playbooks in check mode using ansible-playbook --check --diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs.

## Installation

### Any Agent (npx)
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

### OpenClaw
```bash
clawhub install ansible-playbook-dryrun-validator-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dryrun-validator-agent -a codex
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | Security Reviewed |
| **Rating** | ⭐ 4.9 (79 reviews) |

## Creator

**Ben Taylor**

- Handle: `@bentaylor`
- Profile: [View on ASE](https://agentskillexchange.com/creator/bentaylor/)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
