---
name: "Systemd Service Diagnostics"
description: "Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/systemd-service-diagnostics/"
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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install systemd-service-diagnostics
```

## Source

- Marketplace: https://agentskillexchange.com/skills/systemd-service-diagnostics/
