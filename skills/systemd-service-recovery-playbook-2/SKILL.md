---
name: "Systemd Service Recovery Playbook"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
---
# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

The Systemd Service Recovery Playbook skill automates diagnosis and recovery of failed Linux services managed by systemd. It uses systemctl, journalctl, and the systemd D-Bus API (org.freedesktop.systemd1) for comprehensive service analysis.

The diagnostic sequence: queries systemctl show for ActiveState, SubState, ExecMainStatus, and NRestarts; fetches structured journal entries via journalctl -u service –output=json for pattern matching; analyzes the dependency tree via systemctl list-dependencies –reverse; and checks cgroup resource consumption via systemd-cgtop data.

Common failure patterns handled include: exit code 137 (OOM killed) with MemoryMax/MemoryHigh cgroup limit analysis, socket activation failures with ListenStream/ListenDatagram binding issues, Type=notify services failing watchdog with WatchdogSec timeout analysis, and mount dependency failures with RequiresMountsFor resolution.

The skill generates recovery actions: systemctl reset-failed followed by conditional restart, journal-based log rotation if disk space caused failures, and dynamic property adjustment via systemctl set-property for resource limits. It handles both system and user service managers, supports drop-in override generation in /etc/systemd/system/service.d/, and creates timer-based health check units for persistent issues.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a codex
```

### OpenClaw

```bash
clawhub install systemd-service-recovery-playbook-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/)
