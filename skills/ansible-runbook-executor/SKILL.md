---
name: "Ansible Runbook Executor"
description: "Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ansible-runbook-executor/"
---
# Ansible Runbook Executor

Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming.

## Overview

The Ansible Runbook Executor agent leverages the ansible-runner Python SDK to execute diagnostic and remediation playbooks on remote infrastructure. It parses YAML-based inventory files, resolves host groups, and manages vault-encrypted secrets for secure credential handling during execution.

Designed for incident response, the agent can run pre-defined runbooks for common scenarios: disk space cleanup, service restarts, log collection, certificate rotation, and DNS resolution checks. Each playbook execution produces structured JSON output with per-host task results, return codes, and stdout/stderr capture.

The agent streams real-time task output via ansible-runner event handlers, enabling live progress tracking during long-running operations. It supports check mode (dry-run) for validation before applying changes, and integrates with Ansible Galaxy for pulling community roles. Tags and limits can be applied dynamically to scope execution to specific hosts or task subsets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-runbook-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-runbook-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-runbook-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-runbook-executor -a codex
```

### OpenClaw

```bash
clawhub install ansible-runbook-executor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-runbook-executor/)
