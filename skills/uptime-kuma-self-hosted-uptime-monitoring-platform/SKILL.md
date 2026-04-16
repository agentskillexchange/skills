---
title: "Uptime Kuma Self-Hosted Uptime Monitoring Platform"
description: "Uptime Kuma is an open source uptime monitor for HTTP, TCP, ping, DNS, Docker, and keyword checks. It gives agents a concrete way to create, update, and review monitors, incidents, notifications, and public status pages from a self-hosted monitoring stack."
verification: "security_reviewed"
source: "https://github.com/louislam/uptime-kuma"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "louislam/uptime-kuma"
  github_stars: 85143
  ase_npm_package: "uptime-kuma"
  npm_weekly_downloads: 97
---

# Uptime Kuma Self-Hosted Uptime Monitoring Platform

Uptime Kuma is a self-hosted monitoring platform maintained by louislam and published as the louislam/uptime-kuma project on GitHub. It is built for teams that want a lightweight but capable uptime tool they can run themselves instead of outsourcing checks and status pages to a hosted SaaS. The project supports HTTP and HTTPS checks, TCP port checks, ping, DNS monitoring, Docker container health monitoring, keyword validation, certificate expiration alerts, and public status pages. For an agent workflow, that gives a clear job-to-be-done: create monitors, validate whether a service is reachable, inspect recent incidents, confirm whether latency or certificate state changed, and route alerts into the rest of an operations stack.

The upstream installation guidance supports both Docker and a direct Node.js path. The official install wiki shows a one-command Docker startup, plus a source-based path using Node.js, Git, and PM2. That matters for real-world agent use because the same skill can fit quick local testing, a long-running homelab deployment, or a production monitor running behind a reverse proxy. Uptime Kuma also exposes status pages that agents can update or inspect when they need a user-facing incident summary. Its GitHub repository is active, has an MIT license, and has very strong adoption, which makes it a durable intake candidate rather than a speculative one. Agents that handle incident triage, release verification, cron health checks, or post-deploy smoke monitoring can integrate with Uptime Kuma as a stable source of truth for service availability.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/uptime-kuma-self-hosted-uptime-monitoring-platform/)
