---
name: Systemd Service Diagnostics
description: Diagnoses systemd service failures using journalctl structured JSON output
  and systemctl show properties. Analyzes unit file configurations with systemd-analyze
  verify and detects dependency ordering issues via systemd-analyze dot.
verification: security_reviewed
source: https://agentskillexchange.com/skills/systemd-service-diagnostics/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# Systemd Service Diagnostics

The Systemd Service Diagnostics skill provides comprehensive troubleshooting for Linux systemd service management. It queries service status using systemctl show with machine-readable property output, then correlates failures with structured log data from journalctl -output=json.
The skill handles common failure patterns: services stuck in activating state (analyzing ExecStartPre dependencies), repeated restart loops (checking RestartSec and StartLimitBurst configurations), socket activation failures (verifying ListenStream bindings), and permission denied errors (auditing User/Group, CapabilityBoundingSet, and SELinux/AppArmor contexts).
Unit file analysis uses systemd-analyze verify to detect configuration errors, systemd-analyze security to score service sandboxing (ProtectSystem, PrivateTmp, NoNewPrivileges), and systemd-analyze dot to generate dependency graphs that reveal ordering issues and circular dependencies.
The skill can compare unit file configurations across environments using systemd-delta to identify local overrides, and generates drop-in override files (systemctl edit) for safe configuration modifications without modifying vendor unit files.
Additional capabilities include resource usage analysis via systemd-cgtop correlation, timer unit scheduling validation (OnCalendar expression parsing), and automated generation of hardened unit files following CIS benchmark recommendations for service isolation.
Works with systemd 245+ on all major Linux distributions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-diagnostics/)
