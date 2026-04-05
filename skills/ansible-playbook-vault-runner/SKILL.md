---
name: "Ansible Playbook Runner with Vault Secrets"
description: "Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs."
category: "Runbooks &amp; Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-playbook-vault-runner/"
---
# Ansible Playbook Runner with Vault Secrets

Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-vault-runner -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-vault-runner
```

## Details

Ansible Playbook Runner with Vault Secrets is built around Ansible automation engine. The underlying ecosystem is represented by ansible/ansible (68,365+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like ansible-playbook CLI, inventories, roles, Vault, dynamic inventory plugins and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to ansible so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Executes Ansible playbooks against dynamic inventories from AWS EC2 or Azure, decrypting Ansible Vault secrets via HashiCorp Vault KV v2 API. Streams task output in real time and posts a per-host pass/fail summary to Slack. Supports –check mode for dry-run validation before live runs. The implementation typically relies on ansible-playbook CLI, inventories, roles, Vault, dynamic inventory plugins, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses ansible-playbook CLI, inventories, roles, Vault, dynamic inventory plugins instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as SSH-based infrastructure automation, config management, idempotent change execution.

 Key integration points include SSH-based infrastructure automation, config management, idempotent change execution. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-vault-runner/)
