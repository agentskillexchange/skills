---
name: "Ansible Playbook Dry-Run Analyzer"
description: "Executes ansible-playbook –check –diff mode and parses the JSON callback output using the ansible.posix.json callback plugin. Identifies tasks that would change, predicts idempotency issues, and generates change impact reports."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/"
tool_ecosystem:
  tool: "ansible"
  github_stars: 68365
  npm_weekly_downloads: 0
  github_repo: "ansible/ansible"
  license: "GPL-3.0"
  maintained: true
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [ansible](https://github.com/ansible/ansible) — ⭐ 68.4k · GPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dry-run-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
