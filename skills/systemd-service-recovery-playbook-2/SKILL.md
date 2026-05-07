---
title: "Systemd Service Recovery Playbook"
slug: "systemd-service-recovery-playbook-2"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
verification: security_reviewed
source: "https://github.com/systemd/systemd"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "systemd/systemd"
  github_stars: 16248
---
# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
