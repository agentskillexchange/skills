---
title: "Selenium Grid Load Balancer"
description: "Distributes browser automation workloads across Selenium Grid 4 nodes using the Grid REST API and session queue management. Implements weighted round-robin with health-check monitoring via /status endpoint."
slug: "selenium-grid-load-balancer"
category:
  - "Browser Automation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-load-balancer/"
listed: true
---

# Selenium Grid Load Balancer

Distributes browser automation workloads across Selenium Grid 4 nodes using the Grid REST API and session queue management. Implements weighted round-robin with health-check monitoring via /status endpoint.

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
clawhub install selenium-grid-load-balancer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Load Balancer optimizes test distribution across multiple Selenium Grid 4 nodes. It queries the Grid Hub’s /status REST API endpoint to monitor node capacity, active sessions, and browser availability in real time. The skill implements a weighted round-robin algorithm that factors in node CPU usage, memory availability, and current session count. When a new WebDriver session is requested, the balancer routes it to the least-loaded node that supports the requested browser capability. Health checks run every 10 seconds via HTTP polling of each node’s /wd/hub/status endpoint, automatically removing unresponsive nodes from the rotation. The skill supports dynamic node registration and deregistration through the Grid’s event bus, scaling capacity based on queue depth. It includes configurable thresholds for max sessions per node, queue timeout limits, and automatic session cleanup for orphaned browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration with Grafana monitoring stacks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-load-balancer/)
