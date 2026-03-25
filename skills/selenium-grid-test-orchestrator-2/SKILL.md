---
name: "Selenium Grid Test Orchestrator"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid API. Manages session queuing, node health, and parallel test execution via the WebDriver protocol."
category: "Browser Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/"
tool_ecosystem:
  tool: "selenium"
  github_stars: 34174
  npm_weekly_downloads: 2000657
  github_repo: "SeleniumHQ/selenium"
  license: "Apache-2.0"
  maintained: true
---

# Selenium Grid Test Orchestrator

Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid API. Manages session queuing, node health, and parallel test execution via the WebDriver protocol.

## Overview

Distributed browser test orchestration agent for Selenium Grid 4 infrastructure. Manages test session distribution across grid nodes using the Selenium Grid GraphQL API and New Session Queue endpoints. Monitors node health and availability through the Grid status API with automatic session redistribution on node failures. Configures browser capabilities including Chrome DevTools Protocol integration for network interception and performance profiling. Supports parallel test execution with configurable concurrency limits per browser type. Generates comprehensive test reports with screenshots, console logs, and network HAR files captured via the WebDriver BiDi protocol. Includes smart test retry logic with flaky test detection based on historical pass rates. Integrates with Docker Compose for ephemeral grid provisioning and Kubernetes Helm charts for cloud-scale deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-test-orchestrator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-test-orchestrator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-test-orchestrator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-test-orchestrator-2 -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-test-orchestrator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/
