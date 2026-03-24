---
name: "Ansible Playbook Diagnostics Runner"
description: "Runs Ansible diagnostic playbooks using ansible-runner and the Ansible Collections ecosystem (ansible.builtin, community.general). Captures system health, service status, and log analysis across inventory hosts."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ansible-playbook-diagnostics-runner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "ansible"  # from ase_tool_match
  github_stars: 68365  # from ase_github_stars (integer, not string)
  github_repo: "ansible/ansible"  # from ase_github_repo
  license: "GPL-3.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Ansible Playbook Diagnostics Runner

Runs Ansible diagnostic playbooks using ansible-runner and the Ansible Collections ecosystem (ansible.builtin, community.general). Captures system health, service status, and log analysis across inventory hosts.

## Overview

The Ansible Playbook Diagnostics Runner skill executes diagnostic playbooks using ansible-runner (ansible_runner.run()) and the Ansible automation framework. It leverages modules from ansible.builtin (command, shell, copy, template, service, systemd) and community.general (ufw, nmcli, sysctl, modprobe) collections to perform comprehensive system diagnostics.

The skill manages inventory through dynamic inventory plugins (aws_ec2, azure_rm, gcp_compute) and static YAML/INI inventory files. It executes health check playbooks that gather facts using ansible.builtin.setup, check service status with ansible.builtin.systemd, analyze disk usage via ansible.builtin.command (df, du), and collect log entries using ansible.builtin.shell with journalctl queries.

Advanced capabilities include role-based diagnostic suites organized as Ansible roles with tasks/handlers/defaults/vars, callback plugin integration for custom output formatting (json, yaml, timer), vault-encrypted variable management for sensitive credentials, and async task execution for long-running diagnostics with poll intervals. The runner also supports check mode (–check) for dry-run validation, diff mode (–diff) for configuration drift detection, and custom filter plugins for log parsing and metric extraction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-diagnostics-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-diagnostics-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-diagnostics-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ansible-playbook-diagnostics-runner -a codex
```

### OpenClaw

```bash
clawhub install ansible-playbook-diagnostics-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ansible-playbook-diagnostics-runner/
