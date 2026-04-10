---
title: "Selenium Grid Auto-Scaling Orchestrator"
description: "Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring."
slug: "selenium-grid-auto-scaling-orchestrator"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/"
listed: true
---

# Selenium Grid Auto-Scaling Orchestrator

Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring.

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
clawhub install selenium-grid-auto-scaling-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization.
When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub.
Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints.
The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/)
