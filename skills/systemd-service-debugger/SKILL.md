---
name: Systemd Service Debugger
description: Debugs failed systemd services using journalctl, systemctl, and the systemd
  D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and
  generates fix recommendations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/systemd-service-debugger/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# Systemd Service Debugger

The Systemd Service Debugger skill provides automated diagnosis of failed systemd services on Linux systems. It uses journalctl for log analysis, systemctl for unit status inspection, and the systemd D-Bus org.freedesktop.systemd1 API for deep introspection of unit properties and dependency chains.
When a service enters failed state, the skill retrieves the full journal output using journalctl -u {service} -since {timestamp} with structured JSON output format. It parses ExecStart command failures, identifying common issues like missing binaries, permission denied errors, port binding conflicts, and missing configuration files.
Dependency analysis walks the unit After/Requires/Wants chain using the org.freedesktop.systemd1.Manager.GetUnit D-Bus method to identify cascading failures. Resource limit checking compares configured LimitNOFILE, MemoryMax, and CPUQuota values against actual usage from systemd-cgtop data. The skill also validates socket activation configurations, checks SELinux/AppArmor contexts, and inspects namespace isolation settings. Each diagnosis includes a priority-ranked list of remediation steps with the exact commands to execute.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-debugger/)
