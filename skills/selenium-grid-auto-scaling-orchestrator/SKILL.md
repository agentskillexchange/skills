---
name: "Selenium Grid Auto-Scaling Orchestrator"
description: "Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring."
category: "Browser Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
tool_ecosystem:
  tool: selenium
  github_stars: 34174
  npm_weekly_downloads: 2000657
  github_repo: SeleniumHQ/selenium
  license: Apache-2.0
  maintained: true
---

# Selenium Grid Auto-Scaling Orchestrator

Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring.

## Overview

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization.

When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub.

Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints.

The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-auto-scaling-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-auto-scaling-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-auto-scaling-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-auto-scaling-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-auto-scaling-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/
