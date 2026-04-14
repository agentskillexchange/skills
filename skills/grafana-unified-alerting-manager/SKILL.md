---
title: "Grafana Unified Alerting Manager"
description: "Manages Grafana Unified Alerting rules, contact points, and notification policies via the Grafana HTTP API. Supports alert rule provisioning and silence management across multiple Grafana instances."
verification: security_reviewed
source: "https://github.com/grafana/grafana"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grafana/grafana"
  github_stars: 73187
---

# Grafana Unified Alerting Manager

The Grafana Unified Alerting Manager skill provides full lifecycle management of alerting configurations across Grafana instances using the Grafana Alerting HTTP API. It creates and updates alert rules with PromQL, LogQL, or SQL expressions, configures contact points for email, Slack, PagerDuty, and webhook receivers, and manages notification policies with label-based routing trees. The skill supports alert rule provisioning via the Provisioning API for GitOps workflows, silence creation and expiry management, and mute timing configurations for maintenance windows. Features include bulk rule import/export in JSON and YAML formats, alert rule testing with sample data evaluation, and cross-instance rule synchronization for high-availability Grafana deployments. Integrates with Grafana OnCall API for escalation chain management.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/grafana-unified-alerting-manager/)
