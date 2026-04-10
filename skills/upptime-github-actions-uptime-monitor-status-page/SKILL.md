---
title: "Upptime GitHub Actions Uptime Monitor and Status Page"
description: "An ASE skill built around Upptime, the open source uptime monitor and status page system powered by GitHub Actions, Issues, and Pages. It is a strong fit when an agent needs lightweight endpoint monitoring, incident issue tracking, and a public or internal status site without maintaining a separate monitoring server."
slug: "upptime-github-actions-uptime-monitor-status-page"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/upptime/upptime"
listed: true
---

# Upptime GitHub Actions Uptime Monitor and Status Page

An ASE skill built around Upptime, the open source uptime monitor and status page system powered by GitHub Actions, Issues, and Pages. It is a strong fit when an agent needs lightweight endpoint monitoring, incident issue tracking, and a public or internal status site without maintaining a separate monitoring server.

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
clawhub install upptime-github-actions-uptime-monitor-status-page
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Upptime GitHub Actions Uptime Monitor and Status Page is a source-backed ASE skill for teams that want agent-friendly monitoring without standing up another always-on service. Upptime is maintained in the upptime/upptime repository and documented at upptime.js.org. Its core design is unusually practical: scheduled GitHub Actions workflows check your endpoints every few minutes, response-time history is committed back into the repository, GitHub Issues are opened and closed for incidents, and GitHub Pages publishes the status site.
The job-to-be-done is clear. An agent can configure endpoint checks, review recent outages, summarize incident timelines from GitHub Issues, audit response-time trends, and update monitoring config in version control. This works especially well for developer-facing systems, API health dashboards, SaaS status pages, and internal infrastructure where a git-native audit trail matters. Because the monitor definitions, incident history, and generated status artifacts all live in one repository, the workflow is inspectable and easy to automate.
Integration points include GitHub Actions, GitHub Issues, GitHub Pages, repository secrets, and notification workflows such as Slack. Upptime also has real adoption, current maintenance, official documentation, tagged releases, and a permissive MIT license. For ASE, that makes it a concrete, verifiable monitoring skill anchored to a real upstream project instead of a vague “uptime bot” abstraction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upptime-github-actions-uptime-monitor-status-page/)
