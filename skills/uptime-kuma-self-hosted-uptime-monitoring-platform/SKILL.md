---
title: "Uptime Kuma Self-Hosted Uptime Monitoring Platform"
description: "Uptime Kuma is an open source uptime monitor for HTTP, TCP, ping, DNS, Docker, and keyword checks. It gives agents a concrete way to create, update, and review monitors, incidents, notifications, and public status pages from a self-hosted monitoring stack."
slug: "uptime-kuma-self-hosted-uptime-monitoring-platform"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/louislam/uptime-kuma"
tool_ecosystem:
  github_repo: "louislam/uptime-kuma"
  github_stars: 85056
  npm_package: "uptime-kuma"
  npm_weekly_downloads: 85
listed: true
---

# Uptime Kuma Self-Hosted Uptime Monitoring Platform

Uptime Kuma is an open source uptime monitor for HTTP, TCP, ping, DNS, Docker, and keyword checks. It gives agents a concrete way to create, update, and review monitors, incidents, notifications, and public status pages from a self-hosted monitoring stack.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install uptime-kuma-self-hosted-uptime-monitoring-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Uptime Kuma is a self-hosted monitoring platform maintained by louislam and published as the louislam/uptime-kuma project on GitHub. It is built for teams that want a lightweight but capable uptime tool they can run themselves instead of outsourcing checks and status pages to a hosted SaaS. The project supports HTTP and HTTPS checks, TCP port checks, ping, DNS monitoring, Docker container health monitoring, keyword validation, certificate expiration alerts, and public status pages. For an agent workflow, that gives a clear job-to-be-done: create monitors, validate whether a service is reachable, inspect recent incidents, confirm whether latency or certificate state changed, and route alerts into the rest of an operations stack.
The upstream installation guidance supports both Docker and a direct Node.js path. The official install wiki shows a one-command Docker startup, plus a source-based path using Node.js, Git, and PM2. That matters for real-world agent use because the same skill can fit quick local testing, a long-running homelab deployment, or a production monitor running behind a reverse proxy. Uptime Kuma also exposes status pages that agents can update or inspect when they need a user-facing incident summary. Its GitHub repository is active, has an MIT license, and has very strong adoption, which makes it a durable intake candidate rather than a speculative one. Agents that handle incident triage, release verification, cron health checks, or post-deploy smoke monitoring can integrate with Uptime Kuma as a stable source of truth for service availability.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-self-hosted-uptime-monitoring-platform/)
