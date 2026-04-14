---
title: "Ansible Runbook Executor"
description: "Executes Ansible playbooks for server diagnostics and remediation using ansible-runner Python SDK. Supports inventory parsing, vault-encrypted credentials, and real-time task output streaming."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Runbook Executor

The Ansible Runbook Executor agent leverages the ansible-runner Python SDK to execute diagnostic and remediation playbooks on remote infrastructure. It parses YAML-based inventory files, resolves host groups, and manages vault-encrypted secrets for secure credential handling during execution.

Designed for incident response, the agent can run pre-defined runbooks for common scenarios: disk space cleanup, service restarts, log collection, certificate rotation, and DNS resolution checks. Each playbook execution produces structured JSON output with per-host task results, return codes, and stdout/stderr capture.

The agent streams real-time task output via ansible-runner event handlers, enabling live progress tracking during long-running operations. It supports check mode (dry-run) for validation before applying changes, and integrates with Ansible Galaxy for pulling community roles. Tags and limits can be applied dynamically to scope execution to specific hosts or task subsets.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-runbook-executor/)
