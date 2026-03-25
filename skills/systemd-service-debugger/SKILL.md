---
name: "Systemd Service Debugger"
description: "Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/systemd-service-debugger/"
---

# Systemd Service Debugger

Debugs failed systemd services using journalctl, systemctl, and the systemd D-Bus API. Analyzes unit dependencies, ExecStart failures, resource limits, and generates fix recommendations.

## Overview

The Systemd Service Debugger skill provides automated diagnosis of failed systemd services on Linux systems. It uses journalctl for log analysis, systemctl for unit status inspection, and the systemd D-Bus org.freedesktop.systemd1 API for deep introspection of unit properties and dependency chains.

When a service enters failed state, the skill retrieves the full journal output using journalctl -u {service} –since {timestamp} with structured JSON output format. It parses ExecStart command failures, identifying common issues like missing binaries, permission denied errors, port binding conflicts, and missing configuration files.

Dependency analysis walks the unit After/Requires/Wants chain using the org.freedesktop.systemd1.Manager.GetUnit D-Bus method to identify cascading failures. Resource limit checking compares configured LimitNOFILE, MemoryMax, and CPUQuota values against actual usage from systemd-cgtop data. The skill also validates socket activation configurations, checks SELinux/AppArmor contexts, and inspects namespace isolation settings. Each diagnosis includes a priority-ranked list of remediation steps with the exact commands to execute.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill systemd-service-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill systemd-service-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill systemd-service-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill systemd-service-debugger -a codex
```

### OpenClaw

```bash
clawhub install systemd-service-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/systemd-service-debugger/
