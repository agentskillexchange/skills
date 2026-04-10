---
name: "Upptime GitHub Actions Uptime Monitor and Status Page"
description: "An ASE skill built around Upptime, the open source uptime monitor and status page system powered by GitHub Actions, Issues, and Pages. It is a strong fit when an agent needs lightweight endpoint monitoring, incident issue tracking, and a public or internal status site without maintaining a separate monitoring server."
verification: security_reviewed
source: "https://github.com/upptime/upptime"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
---

# Upptime GitHub Actions Uptime Monitor and Status Page

Upptime GitHub Actions Uptime Monitor and Status Page is a source-backed ASE skill for teams that want agent-friendly monitoring without standing up another always-on service. Upptime is maintained in the upptime/upptime repository and documented at upptime.js.org. Its core design is unusually practical: scheduled GitHub Actions workflows check your endpoints every few minutes, response-time history is committed back into the repository, GitHub Issues are opened and closed for incidents, and GitHub Pages publishes the status site.
The job-to-be-done is clear. An agent can configure endpoint checks, review recent outages, summarize incident timelines from GitHub Issues, audit response-time trends, and update monitoring config in version control. This works especially well for developer-facing systems, API health dashboards, SaaS status pages, and internal infrastructure where a git-native audit trail matters. Because the monitor definitions, incident history, and generated status artifacts all live in one repository, the workflow is inspectable and easy to automate.
Integration points include GitHub Actions, GitHub Issues, GitHub Pages, repository secrets, and notification workflows such as Slack. Upptime also has real adoption, current maintenance, official documentation, tagged releases, and a permissive MIT license. For ASE, that makes it a concrete, verifiable monitoring skill anchored to a real upstream project instead of a vague “uptime bot” abstraction.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upptime-github-actions-uptime-monitor-status-page/)
