---
name: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and ge..."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "security_reviewed"
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/ansible-playbook-dry-run-analyzer/"
---

# Ansible Playbook Dry-Run Analyzer

Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports.

## Installation

Install this skill across different agents:

### Any Agent (npx)
```bash
npx @anthropic/skills install ansible-playbook-dry-run-analyzer
```

### Claude Code
```bash
claude skills add ansible-playbook-dry-run-analyzer
```

### Cursor
Add to your `.cursor/skills/` directory or install via Cursor settings.

### OpenClaw
```bash
clawhub install ansible-playbook-dry-run-analyzer
```

### Codex
```bash
codex skills add ansible-playbook-dry-run-analyzer
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

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/ansible-playbook-dry-run-analyzer/)
- [Browse All Skills](https://agentskillexchange.com/)
