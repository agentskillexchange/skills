---
name: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-vault-runner/"
tool_ecosystem:
  tool: "ansible"
  github_stars: 68365
  npm_weekly_downloads: 9204385
  github_repo: "ansible/ansible"
  license: "GPL-3.0"
  maintained: true
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a cursor
```

### OpenClaw
```bash
clawhub install ansible-playbook-vault-runner
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [ansible](https://github.com/ansible/ansible) — ⭐ 68.4k · GPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
