---
title: "Prometheus AlertManager Router"
description: "Configures and manages Prometheus AlertManager routing trees and silences via the AlertManager HTTP API. Supports PagerDuty, OpsGenie, and Slack receiver configuration with inhibition rules."
verification: security_reviewed
source: "https://github.com/prometheus/prometheus"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "prometheus/prometheus"
  github_stars: 63584
---

# Prometheus AlertManager Router

The Prometheus AlertManager Router skill provides intelligent alert routing and management through the AlertManager HTTP API. It enables agents to programmatically create, modify, and debug complex routing trees that determine how alerts flow from Prometheus to notification receivers like PagerDuty, OpsGenie, Slack, and email.

Key features include routing tree visualization and validation before applying changes, automatic silence creation during maintenance windows with scheduled expiry, and inhibition rule management to suppress dependent alerts when root-cause alerts are already firing. The skill can analyze alert group patterns to suggest routing optimizations.

It supports match and match_re label-based routing, continue flags for multi-receiver fan-out, group_by/group_wait/group_interval tuning for alert batching, and receiver template customization using Go template syntax. Integration with Prometheus’s /api/v1/rules endpoint enables correlation between recording rules, alerting rules, and their AlertManager routing destinations for end-to-end observability pipeline verification.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alertmanager-router/)
