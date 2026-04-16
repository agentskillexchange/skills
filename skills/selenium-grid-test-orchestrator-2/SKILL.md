---
title: "Selenium Grid Test Orchestrator"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid API. Manages session queuing, node health, and parallel test execution via the WebDriver protocol."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  license: "Apache-2.0"
---

# Selenium Grid Test Orchestrator

Distributed browser test orchestration agent for Selenium Grid 4 infrastructure. Manages test session distribution across grid nodes using the Selenium Grid GraphQL API and New Session Queue endpoints. Monitors node health and availability through the Grid status API with automatic session redistribution on node failures. Configures browser capabilities including Chrome DevTools Protocol integration for network interception and performance profiling. Supports parallel test execution with configurable concurrency limits per browser type. Generates comprehensive test reports with screenshots, console logs, and network HAR files captured via the WebDriver BiDi protocol. Includes smart test retry logic with flaky test detection based on historical pass rates. Integrates with Docker Compose for ephemeral grid provisioning and Kubernetes Helm charts for cloud-scale deployments.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/)
