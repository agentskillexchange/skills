---
title: "Systemd Service Debugger"
description: "Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations."
verification: security_reviewed
source: "https://github.com/systemd/systemd"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "systemd/systemd"
  github_stars: 16248
---

# Systemd Service Debugger

Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/systemd-service-debugger/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/systemd-service-debugger
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/systemd-service-debugger`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-debugger/)
