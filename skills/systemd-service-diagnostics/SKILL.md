---
name: Systemd Service Diagnostics
description: Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering 
category: Runbooks & Diagnostics
framework: OpenClaw
verification: security_reviewed
rating: 4.9
reviews: 69
source: https://agentskillexchange.com/skill/systemd-service-diagnostics/
---

# Systemd Service Diagnostics

Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot.

## Overview

The Systemd Service Diagnostics skill provides comprehensive troubleshooting for Linux systemd service management. It queries service status using systemctl show with machine-readable property output, then correlates failures with structured log data from journalctl –output=json.
The skill handles common failure patterns: services stuck in activating state (analyzing ExecStartPre dependencies), repeated restart loops (checking RestartSec and StartLimitBurst configurations), socket activation failures (verifying ListenStream bindings), and permission denied errors (auditing User/Group, CapabilityBoundingSet, and SELinux/AppArmor contexts).
Unit file analysis uses systemd-analyze verify to detect configuration errors, systemd-analyze security to score service sandboxing (ProtectSystem, PrivateTmp, NoNewPrivileges), and systemd-analyze dot to generate dependency graphs that reveal ordering issues and circular dependencies.
The skill can compare unit file configurations across environments using systemd-delta to identify local overrides, and generates drop-in override files (systemctl edit) for safe configuration modifications without modifying vendor unit files.
Additional capabilities include resource usage analysis via systemd-cgtop correlation, timer unit scheduling validation (OnCalendar expression parsing), and automated generation of hardened unit files following CIS benchmark recommendations for service isolation.
Works with systemd 245+ on all major Linux distributions.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics
```

### OpenClaw

```bash
openclaw install systemd-service-diagnostics
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (69 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/systemd-service-diagnostics/)*
