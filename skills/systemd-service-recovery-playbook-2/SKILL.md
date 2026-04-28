---
title: Systemd Service Recovery Playbook
description: Diagnoses and recovers failed systemd services using journalctl, systemctl
  status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency
  chains via list-dependencies, and resource limits from cgroup controllers.
verification: security_reviewed
source: https://github.com/systemd/systemd
category:
- Runbooks & Diagnostics
framework:
- ChatGPT Agents
tool_ecosystem:
  github_repo: systemd/systemd
  github_stars: 16248
---

# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/systemd-service-recovery-playbook-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/systemd-service-recovery-playbook-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
