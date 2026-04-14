---
title: "Selenium Grid Test Orchestrator"
description: "Orchestrates distributed browser testing across Selenium Grid 4 nodes using the Grid API. Manages session queuing, node health, and parallel test execution via the WebDriver protocol."
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "seleniumhq/selenium"
  github_stars: 34076
  npm_package: "selenium-webdriver"
  npm_weekly_downloads: 1932148
---

# Selenium Grid Test Orchestrator

Distributed browser test orchestration agent for Selenium Grid 4 infrastructure. Manages test session distribution across grid nodes using the Selenium Grid GraphQL API and New Session Queue endpoints. Monitors node health and availability through the Grid status API with automatic session redistribution on node failures. Configures browser capabilities including Chrome DevTools Protocol integration for network interception and performance profiling. Supports parallel test execution with configurable concurrency limits per browser type. Generates comprehensive test reports with screenshots, console logs, and network HAR files captured via the WebDriver BiDi protocol. Includes smart test retry logic with flaky test detection based on historical pass rates. Integrates with Docker Compose for ephemeral grid provisioning and Kubernetes Helm charts for cloud-scale deployments.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-test-orchestrator-2/)
