---
title: "Systemd Service Diagnostics"
description: "The Systemd Service Diagnostics skill provides comprehensive troubleshooting for Linux systemd service management. It queries service status using systemctl show with machine-readable property output, then correlates failures with structured log data from journalctl &#8211;output=json. The skill handles common failure patterns: services stuck in activating state (analyzing ExecStartPre dependencies), repeated restart loops (checking RestartSec and StartLimitBurst configurations), socket activation failures (verifying ListenStream bindings), and permission denied errors (auditing User/Group, CapabilityBoundingSet, and SELinux/AppArmor contexts). Unit file analysis uses systemd-analyze verify to detect configuration errors, systemd-analyze security to score service sandboxing (ProtectSystem, PrivateTmp, NoNewPrivileges), and systemd-analyze dot to generate dependency graphs that reveal ordering issues and circular dependencies. The skill can compare unit file configurations across environments using systemd-delta to identify local overrides, and generates drop-in override files (systemctl edit) for safe configuration modifications without modifying vendor unit files. Additional capabilities include resource usage analysis via systemd-cgtop correlation, timer unit scheduling validation (OnCalendar expression parsing), and automated generation of hardened unit files following CIS benchmark recommendations for service isolation. Works with systemd 245+ on all major Linux distributions."
source: "https://agentskillexchange.com/skills/systemd-service-diagnostics/"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Systemd Service Diagnostics

The Systemd Service Diagnostics skill provides comprehensive troubleshooting for Linux systemd service management. It queries service status using systemctl show with machine-readable property output, then correlates failures with structured log data from journalctl &#8211;output=json. The skill handles common failure patterns: services stuck in activating state (analyzing ExecStartPre dependencies), repeated restart loops (checking RestartSec and StartLimitBurst configurations), socket activation failures (verifying ListenStream bindings), and permission denied errors (auditing User/Group, CapabilityBoundingSet, and SELinux/AppArmor contexts). Unit file analysis uses systemd-analyze verify to detect configuration errors, systemd-analyze security to score service sandboxing (ProtectSystem, PrivateTmp, NoNewPrivileges), and systemd-analyze dot to generate dependency graphs that reveal ordering issues and circular dependencies. The skill can compare unit file configurations across environments using systemd-delta to identify local overrides, and generates drop-in override files (systemctl edit) for safe configuration modifications without modifying vendor unit files. Additional capabilities include resource usage analysis via systemd-cgtop correlation, timer unit scheduling validation (OnCalendar expression parsing), and automated generation of hardened unit files following CIS benchmark recommendations for service isolation. Works with systemd 245+ on all major Linux distributions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-diagnostics/)
