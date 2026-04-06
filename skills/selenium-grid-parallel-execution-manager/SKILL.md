---
name: "Selenium Grid Parallel Execution Manager"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid REST API. Manages session allocation, node health monitoring, and parallel TestNG suite execution."
category: "Browser Automation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/selenium-grid-parallel-execution-manager/"
---
# Selenium Grid Parallel Execution Manager

Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid REST API. Manages session allocation, node health monitoring, and parallel TestNG suite execution.

The Selenium Grid Parallel Execution Manager handles distributed browser test execution across Selenium Grid 4 infrastructure. It communicates with the Grid Hub via the SE4 REST API to monitor node availability, browser capabilities, and session queue depth. The skill dynamically configures TestNG XML suites to maximize parallelism based on available Grid capacity—allocating Chrome, Firefox, and Edge sessions proportionally across registered nodes. It implements smart test distribution using a priority queue that runs flaky or slow tests first, maximizing pipeline efficiency. Session management includes automatic retry logic for node disconnections and stale session cleanup via the Grid drain API. The skill monitors real-time Grid status dashboards through the GraphQL endpoint, tracking session creation latency, queue wait times, and node CPU utilization. It supports Docker-based dynamic Grid scaling by triggering Kubernetes HPA or Docker Compose scale commands when queue depth exceeds configurable thresholds. Test results are aggregated across all nodes into unified Allure reports with screenshots, video recordings via Selenium Video plugin, and browser console logs attached to each test case.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-execution-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-execution-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-execution-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-parallel-execution-manager -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-parallel-execution-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-parallel-execution-manager/)
