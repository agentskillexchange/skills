---
title: "Selenium Grid Auto-Scaling Orchestrator"
description: "The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization. When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub. Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints. The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API."
source: "https://github.com/SeleniumHQ/selenium"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Auto-Scaling Orchestrator

The Selenium Grid Auto-Scaling Orchestrator provides intelligent scaling of Selenium Grid 4 infrastructure based on real-time test demand. It queries the Grid Status API and GraphQL endpoint to monitor session queues, node health, and resource utilization. When queue depth exceeds configurable thresholds, the orchestrator provisions new browser nodes using the Docker Engine API, supporting Chrome (selenium/node-chrome), Firefox (selenium/node-firefox), and Edge (selenium/node-edge) images. Each node is health-checked via the /status endpoint before being registered with the Grid Hub. Scale-down logic uses configurable idle timeouts with graceful session draining — nodes are marked as draining via the Grid Distributor API, allowing running sessions to complete before container removal. Resource limits (CPU, memory) are enforced per container using Docker cgroup constraints. The skill includes Prometheus metrics export for node count, session duration histograms, and queue wait times. Integrates with Kubernetes HPA for cloud deployments using custom metrics from the Selenium Grid GraphQL API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-auto-scaling-orchestrator/)
