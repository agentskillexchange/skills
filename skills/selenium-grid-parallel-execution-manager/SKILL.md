---
title: "Selenium Grid Parallel Execution Manager"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid REST API. Manages session allocation, node health monitoring, and parallel TestNG suite execution."
slug: "selenium-grid-parallel-execution-manager"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/selenium-grid-parallel-execution-manager/"
---

# Selenium Grid Parallel Execution Manager

Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid REST API. Manages session allocation, node health monitoring, and parallel TestNG suite execution.

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
clawhub install selenium-grid-parallel-execution-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Selenium Grid Parallel Execution Manager handles distributed browser test execution across Selenium Grid 4 infrastructure. It communicates with the Grid Hub via the SE4 REST API to monitor node availability, browser capabilities, and session queue depth. The skill dynamically configures TestNG XML suites to maximize parallelism based on available Grid capacity—allocating Chrome, Firefox, and Edge sessions proportionally across registered nodes. It implements smart test distribution using a priority queue that runs flaky or slow tests first, maximizing pipeline efficiency. Session management includes automatic retry logic for node disconnections and stale session cleanup via the Grid drain API. The skill monitors real-time Grid status dashboards through the GraphQL endpoint, tracking session creation latency, queue wait times, and node CPU utilization. It supports Docker-based dynamic Grid scaling by triggering Kubernetes HPA or Docker Compose scale commands when queue depth exceeds configurable thresholds. Test results are aggregated across all nodes into unified Allure reports with screenshots, video recordings via Selenium Video plugin, and browser console logs attached to each test case.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-execution-manager/)
