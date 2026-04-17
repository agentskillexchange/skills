---
title: "Systemd Service Recovery Playbook"
description: "The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis.\nThe diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service –output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies –reverse; and checks cgroup resource consumption via systemd-cgtop data.\nCommon failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution.\nThe skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
framework:
  - "ChatGPT Agents"
---

# Systemd Service Recovery Playbook

The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis.
The diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service –output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies –reverse; and checks cgroup resource consumption via systemd-cgtop data.
Common failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution.
The skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/systemd-service-recovery-playbook-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/systemd-service-recovery-playbook-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
