---
name: "Selenium Grid Load Balancer"
description: "Distributes browser automation workloads across Selenium Grid 4 nodes using the Grid REST API and session queue management. Implements weighted round-robin with health-check monitoring via /status endpoint."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/selenium-grid-load-balancer/"
---
# Selenium Grid Load Balancer

Distributes browser automation workloads across Selenium Grid 4 nodes using the Grid REST API and session queue management. Implements weighted round-robin with health-check monitoring via /status endpoint.

## Overview

The Selenium Grid Load Balancer optimizes test distribution across multiple Selenium Grid 4 nodes. It queries the Grid Hub’s /status REST API endpoint to monitor node capacity, active sessions, and browser availability in real time. The skill implements a weighted round-robin algorithm that factors in node CPU usage, memory availability, and current session count. When a new WebDriver session is requested, the balancer routes it to the least-loaded node that supports the requested browser capability. Health checks run every 10 seconds via HTTP polling of each node’s /wd/hub/status endpoint, automatically removing unresponsive nodes from the rotation. The skill supports dynamic node registration and deregistration through the Grid’s event bus, scaling capacity based on queue depth. It includes configurable thresholds for max sessions per node, queue timeout limits, and automatic session cleanup for orphaned browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration with Grafana monitoring stacks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-load-balancer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-load-balancer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-load-balancer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-load-balancer -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-load-balancer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-load-balancer/)
