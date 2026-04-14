---
title: "Uptime Robot Multi-Check Coordinator"
description: "Manages bulk uptime monitoring via the Uptime Robot API v2. Creates HTTP, keyword, and port monitors with alert contacts, maintenance windows, and status page synchronization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "OpenClaw"
---

# Uptime Robot Multi-Check Coordinator

The Uptime Robot Multi-Check Coordinator manages large-scale uptime monitoring configurations through the Uptime Robot API v2. It supports bulk creation and management of HTTP, HTTPS, keyword, ping, and port monitors across service portfolios. Monitor configurations include custom check intervals, timeout values, and HTTP authentication for protected endpoints. Alert contact management enables routing notifications to appropriate teams via email, Slack, PagerDuty, and webhook integrations with configurable escalation delays. The agent handles maintenance window scheduling to suppress alerts during planned downtime periods. Status page synchronization ensures public-facing status pages reflect current monitor states and incident timelines. Bulk operations support importing monitor configurations from CSV or JSON service catalogs. The tool provides uptime analytics by aggregating response time data and availability percentages across monitor groups. Custom alert thresholds enable differentiated monitoring for critical versus non-critical services with appropriate check frequencies.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-robot-multi-check-coordinator/)
