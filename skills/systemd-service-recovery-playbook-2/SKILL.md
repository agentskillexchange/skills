---
title: "Systemd Service Recovery Playbook"
description: "The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis. The diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service &#8211;output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies &#8211;reverse; and checks cgroup resource consumption via systemd-cgtop data. Common failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution. The skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues."
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
---

# Systemd Service Recovery Playbook

The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis. The diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service &#8211;output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies &#8211;reverse; and checks cgroup resource consumption via systemd-cgtop data. Common failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution. The skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
