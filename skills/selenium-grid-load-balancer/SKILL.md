---
title: "Selenium Grid Load Balancer"
description: "The Selenium Grid Load Balancer optimizes test distribution across multiple Selenium Grid 4 nodes. It queries the Grid Hub&#8217;s /status REST API endpoint to monitor node capacity, active sessions, and browser availability in real time. The skill implements a weighted round-robin algorithm that factors in node CPU usage, memory availability, and current session count. When a new WebDriver session is requested, the balancer routes it to the least-loaded node that supports the requested browser capability. Health checks run every 10 seconds via HTTP polling of each node&#8217;s /wd/hub/status endpoint, automatically removing unresponsive nodes from the rotation. The skill supports dynamic node registration and deregistration through the Grid&#8217;s event bus, scaling capacity based on queue depth. It includes configurable thresholds for max sessions per node, queue timeout limits, and automatic session cleanup for orphaned browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration with Grafana monitoring stacks."
source: "https://github.com/SeleniumHQ/selenium"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Load Balancer

The Selenium Grid Load Balancer optimizes test distribution across multiple Selenium Grid 4 nodes. It queries the Grid Hub&#8217;s /status REST API endpoint to monitor node capacity, active sessions, and browser availability in real time. The skill implements a weighted round-robin algorithm that factors in node CPU usage, memory availability, and current session count. When a new WebDriver session is requested, the balancer routes it to the least-loaded node that supports the requested browser capability. Health checks run every 10 seconds via HTTP polling of each node&#8217;s /wd/hub/status endpoint, automatically removing unresponsive nodes from the rotation. The skill supports dynamic node registration and deregistration through the Grid&#8217;s event bus, scaling capacity based on queue depth. It includes configurable thresholds for max sessions per node, queue timeout limits, and automatic session cleanup for orphaned browsers. Dashboard metrics are exposed via a Prometheus /metrics endpoint for integration with Grafana monitoring stacks.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-load-balancer/)
