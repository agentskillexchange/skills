---
title: "Selenium Grid Auto-Scaling Orchestrator"
description: "Orchestrates Selenium Grid 4 node scaling based on test queue depth using the Grid GraphQL API. Manages Docker container lifecycle for Chrome, Firefox, and Edge nodes with health monitoring."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  ase_npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Auto-Scaling Orchestrator

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization.

When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub.

Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints.

The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-auto-scaling-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/selenium-grid-auto-scaling-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/)
