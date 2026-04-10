---
name: Selenium Grid Test Orchestrator
description: Orchestrates distributed browser testing across Selenium Grid 4 nodes
  using the Grid API. Manages session queuing, node health, and parallel test execution
  via the WebDriver protocol.
verification: security_reviewed
source: https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/
category:
- Browser Automation
framework:
- ChatGPT Agents
---
# Selenium Grid Test Orchestrator

Distributed browser test orchestration agent for Selenium Grid 4 infrastructure. Manages test session distribution across grid nodes using the Selenium Grid GraphQL API and New Session Queue endpoints. Monitors node health and availability through the Grid status API with automatic session redistribution on node failures. Configures browser capabilities including Chrome DevTools Protocol integration for network interception and performance profiling. Supports parallel test execution with configurable concurrency limits per browser type. Generates comprehensive test reports with screenshots, console logs, and network HAR files captured via the WebDriver BiDi protocol. Includes smart test retry logic with flaky test detection based on historical pass rates. Integrates with Docker Compose for ephemeral grid provisioning and Kubernetes Helm charts for cloud-scale deployments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/)
