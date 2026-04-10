---
title: "Ansible Runbook Executor"
description: "Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming."
slug: "ansible-runbook-executor"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ansible-runbook-executor/"
---

# Ansible Runbook Executor

Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ansible-runbook-executor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Ansible Runbook Executor agent leverages the ansible-runner Python SDK to execute diagnostic and remediation playbooks on remote infrastructure. It parses YAML-based inventory files, resolves host groups, and manages vault-encrypted secrets for secure credential handling during execution.
Designed for incident response, the agent can run pre-defined runbooks for common scenarios: disk space cleanup, service restarts, log collection, certificate rotation, and DNS resolution checks. Each playbook execution produces structured JSON output with per-host task results, return codes, and stdout/stderr capture.
The agent streams real-time task output via ansible-runner event handlers, enabling live progress tracking during long-running operations. It supports check mode (dry-run) for validation before applying changes, and integrates with Ansible Galaxy for pulling community roles. Tags and limits can be applied dynamically to scope execution to specific hosts or task subsets.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-runbook-executor/)
