---
title: "Systemd Service Recovery Playbook"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
