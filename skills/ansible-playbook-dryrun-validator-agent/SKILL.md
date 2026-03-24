---
name: "Ansible Playbook Dry-Run Validator"
description: "Validates Ansible playbooks in check mode using ansible-playbook –check –diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/"
tool_ecosystem:
  tool: "ansible"
  github_stars: 68365
  npm_weekly_downloads: 9204385
  github_repo: "ansible/ansible"
  license: "GPL-3.0"
  maintained: true
---

# Ansible Playbook Dry-Run Validator

Validates Ansible playbooks in check mode using ansible-playbook –check –diff and the Ansible Python API. Detects idempotency issues, undefined variables, and unreachable hosts before production runs.

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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [ansible](https://github.com/ansible/ansible) — ⭐ 68.4k · GPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-dryrun-validator-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
