---
name: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: verified_metadata
rating: 4.6
reviews: 52
creator: Isabella Rossi
creator_handle: irossi
creator_verified: false
source: https://agentskillexchange.com/skill/ansible-playbook-vault-runner/
---

# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Verified Metadata |
| Rating | 4.6/5 (52 reviews) |

## Creator

**Isabella Rossi**
- Profile: [@irossi](https://agentskillexchange.com/browse-skills/?creator=irossi)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/ansible-playbook-vault-runner/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
