---
title: "Checkmate Open Source Uptime and Infrastructure Monitoring"
description: "An ASE skill built on Checkmate, the open source self-hosted monitoring platform for uptime, incidents, response times, and infrastructure visibility. It fits agent workflows that need recurring checks, incident context, and operational dashboards with optional server telemetry via the companion Capture agent."
slug: "checkmate-open-source-uptime-infrastructure-monitoring"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/bluewave-labs/Checkmate"
listed: true
---

# Checkmate Open Source Uptime and Infrastructure Monitoring

An ASE skill built on Checkmate, the open source self-hosted monitoring platform for uptime, incidents, response times, and infrastructure visibility. It fits agent workflows that need recurring checks, incident context, and operational dashboards with optional server telemetry via the companion Capture agent.

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
clawhub install checkmate-open-source-uptime-infrastructure-monitoring
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Checkmate Open Source Uptime and Infrastructure Monitoring is a source-backed ASE skill for self-hosted monitoring operations. The upstream project lives at bluewave-labs/Checkmate, with documentation at checkmate.so. Checkmate combines uptime checks, incident tracking, response-time reporting, and infrastructure monitoring in one application, and its README explicitly describes support for monitoring server hardware, websites, and service availability in real time.
The concrete job-to-be-done is operational visibility with actionable incident context. An agent can use Checkmate to inspect monitor health, review downtime events, verify response-time regressions, and summarize current incidents for a human operator. For infrastructure-heavy workflows, Checkmate can also pair with the Capture agent to collect CPU, RAM, disk, and temperature data from remote machines, which gives the agent more than simple HTTP up or down checks. That makes it useful for small hosting setups, internal tools, homelabs, and production services where the team wants one open source monitoring surface.
Integration points include Docker-based deployment, remote server monitoring, dashboards, incident reports, and the Capture telemetry agent. The project has strong adoption, a live documentation portal, tagged releases, and an AGPL license, with active maintenance visible in recent commits. It passes ASE intake as a real, current monitoring tool with a clear operational role for agents.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkmate-open-source-uptime-infrastructure-monitoring/)
