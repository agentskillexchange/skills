---
title: "Systemd Service Recovery Playbook"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
slug: "systemd-service-recovery-playbook-2"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
listed: true
---

# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install systemd-service-recovery-playbook-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis.
The diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service –output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies –reverse; and checks cgroup resource consumption via systemd-cgtop data.
Common failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution.
The skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
