---
title: "Selenium Grid Parallel Execution Manager"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid REST API. Manages session allocation, node health monitoring, and parallel TestNG suite execution."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
  license: "Apache-2.0"
---

# Selenium Grid Parallel Execution Manager

The Selenium Grid Parallel Execution Manager handles distributed browser test execution across Selenium Grid 4 infrastructure. It communicates with the Grid Hub via the SE4 REST API to monitor node availability, browser capabilities, and session queue depth. The skill dynamically configures TestNG XML suites to maximize parallelism based on available Grid capacity—allocating Chrome, Firefox, and Edge sessions proportionally across registered nodes. It implements smart test distribution using a priority queue that runs flaky or slow tests first, maximizing pipeline efficiency. Session management includes automatic retry logic for node disconnections and stale session cleanup via the Grid drain API. The skill monitors real-time Grid status dashboards through the GraphQL endpoint, tracking session creation latency, queue wait times, and node CPU utilization. It supports Docker-based dynamic Grid scaling by triggering Kubernetes HPA or Docker Compose scale commands when queue depth exceeds configurable thresholds. Test results are aggregated across all nodes into unified Allure reports with screenshots, video recordings via Selenium Video plugin, and browser console logs attached to each test case.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/selenium-grid-parallel-execution-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/selenium-grid-parallel-execution-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-execution-manager/)
