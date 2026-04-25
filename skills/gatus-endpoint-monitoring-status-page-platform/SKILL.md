---
title: "Gatus Endpoint Monitoring and Status Page Platform"
description: "Gatus is an open source uptime and endpoint monitoring platform built for developers and ops teams. It checks HTTP, TCP, ICMP, and DNS targets, evaluates conditions like status codes or response times, and can route alerts to systems such as Slack, PagerDuty, Discord, and Twilio."
verification: "security_reviewed"
source: "https://github.com/TwiN/gatus"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "twin/gatus"
  github_stars: 10652
---

# Gatus Endpoint Monitoring and Status Page Platform

Gatus is an open source monitoring platform from the TwiN/gatus project that combines endpoint checks, alerting, and a hosted-style status page in one deployable service. It is designed for engineers who want a lightweight way to watch APIs, websites, certificates, and infrastructure endpoints without wiring together several separate tools. The project supports checks over HTTP, TCP, ICMP, and DNS. Beyond simple uptime probes, it can evaluate conditions against response codes, latency, body content, and certificate expiration. That makes it useful for API smoke checks, internal service health dashboards, and release verification pipelines. The README also documents alert integrations for Slack, Microsoft Teams, PagerDuty, Discord, Twilio, email, Datadog, GitHub, GitLab, and many others, which gives the skill a clear job-to-be-done for teams that need both monitoring and escalation. For agent workflows, Gatus fits well anywhere an assistant needs to validate service availability, surface degraded endpoints, or maintain a human-readable status page backed by concrete checks. It can be deployed quickly with Docker, configured from YAML, and used as a stable health source for CI/CD pipelines, runbooks, and operational automation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gatus-endpoint-monitoring-status-page-platform/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gatus-endpoint-monitoring-status-page-platform
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gatus-endpoint-monitoring-status-page-platform`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gatus-endpoint-monitoring-status-page-platform/)
