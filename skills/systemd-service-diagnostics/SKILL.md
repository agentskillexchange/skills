---
title: "Systemd Service Diagnostics"
description: "Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot."
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

# Systemd Service Diagnostics

Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/systemd-service-diagnostics/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/systemd-service-diagnostics
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/systemd-service-diagnostics`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-diagnostics/)
