---
title: "Systemd Service Recovery Playbook"
slug: "systemd-service-recovery-playbook-2"
verification: "security_reviewed"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
---

# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
