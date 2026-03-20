---
name: Ansible Playbook Diagnostics Runner
description: Runs Ansible diagnostic playbooks using ansible-runner and the Ansible Collections ecosystem (ansible.builtin, community.general). Captures system health, service status, and log analysis across inven
category: Runbooks & Diagnostics
framework: Gemini
verification: security_reviewed
rating: 4.9
reviews: 6
source: https://agentskillexchange.com/skill/ansible-playbook-diagnostics-runner/
---

# Ansible Playbook Diagnostics Runner

Runs Ansible diagnostic playbooks using ansible-runner and the Ansible Collections ecosystem (ansible.builtin, community.general). Captures system health, service status, and log analysis across inventory hosts.

## Overview

The Ansible Playbook Diagnostics Runner skill executes diagnostic playbooks using ansible-runner (ansible_runner.run()) and the Ansible automation framework. It leverages modules from ansible.builtin (command, shell, copy, template, service, systemd) and community.general (ufw, nmcli, sysctl, modprobe) collections to perform comprehensive system diagnostics.
The skill manages inventory through dynamic inventory plugins (aws_ec2, azure_rm, gcp_compute) and static YAML/INI inventory files. It executes health check playbooks that gather facts using ansible.builtin.setup, check service status with ansible.builtin.systemd, analyze disk usage via ansible.builtin.command (df, du), and collect log entries using ansible.builtin.shell with journalctl queries.
Advanced capabilities include role-based diagnostic suites organized as Ansible roles with tasks/handlers/defaults/vars, callback plugin integration for custom output formatting (json, yaml, timer), vault-encrypted variable management for sensitive credentials, and async task execution for long-running diagnostics with poll intervals. The runner also supports check mode (–check) for dry-run validation, diff mode (–diff) for configuration drift detection, and custom filter plugins for log parsing and metric extraction.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-diagnostics-runner
```

### OpenClaw

```bash
openclaw install ansible-playbook-diagnostics-runner
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (6 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/ansible-playbook-diagnostics-runner/)*
