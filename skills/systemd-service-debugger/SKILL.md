---
name: Systemd Service Debugger
description: Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations.
category: Runbooks & Diagnostics
framework: OpenClaw
verification: security_reviewed
rating: 4.8
reviews: 85
source: https://agentskillexchange.com/skill/systemd-service-debugger/
---

# Systemd Service Debugger

Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations.

## Overview

The Systemd Service Debugger skill provides automated diagnosis of failed systemd services on Linux systems. It uses journalctl for log analysis, systemctl for unit status inspection, and the systemd D-Bus org.freedesktop.systemd1 API for deep introspection of unit properties and dependency chains.
When a service enters failed state, the skill retrieves the full journal output using journalctl -u {service} –since {timestamp} with structured JSON output format. It parses ExecStart command failures, identifying common issues like missing binaries, permission denied errors, port binding conflicts, and missing configuration files.
Dependency analysis walks the unit After/Requires/Wants chain using the org.freedesktop.systemd1.Manager.GetUnit D-Bus method to identify cascading failures. Resource limit checking compares configured LimitNOFILE, MemoryMax, and CPUQuota values against actual usage from systemd-cgtop data. The skill also validates socket activation configurations, checks SELinux/AppArmor contexts, and inspects namespace isolation settings. Each diagnosis includes a priority-ranked list of remediation steps with the exact commands to execute.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill systemd-service-debugger
```

### OpenClaw

```bash
openclaw install systemd-service-debugger
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (85 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/systemd-service-debugger/)*
