---
title: "Systemd Service Debugger"
description: "Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations."
verification: "security_reviewed"
source: "https://github.com/systemd/systemd"
author: "systemd"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://systemd.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-debugger/)
