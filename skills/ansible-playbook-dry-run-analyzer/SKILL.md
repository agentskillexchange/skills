---
name: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and ge..."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/"
---
# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

## Installation

### Any Agent (npx)
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

### OpenClaw
```bash
clawhub install ansible-playbook-dry-run-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-dry-run-analyzer -a codex
```
## Details

| Property | Value |
|----------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | security_reviewed |
| **Rating** | 0/5 (0 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/)
- [Browse All Skills](https://agentskillexchange.com/)
