---
name: "Selenium Grid Cloud Executor"
description: "Distributes browser test suites across Selenium Grid 4 nodes using RemoteWebDriver and the W3C WebDriver protocol. Supports parallel execution on BrowserStack and Sauce Labs with automatic capability negotiation."
category: "Browser Automation"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/SeleniumHQ/selenium"
tool_ecosystem:
  tool: selenium
  github_repo: SeleniumHQ/selenium
  github_stars: 34196
  license: Apache-2.0
  maintained: true
---
# Selenium Grid Cloud Executor

Distributes browser test suites across Selenium Grid 4 nodes using RemoteWebDriver and the W3C WebDriver protocol. Supports parallel execution on BrowserStack and Sauce Labs with automatic capability negotiation.

## Overview

This skill enables distributed browser test execution across Selenium Grid 4 infrastructure or cloud providers like BrowserStack and Sauce Labs. It uses the RemoteWebDriver API with the W3C WebDriver protocol for cross-browser compatibility testing at scale.

The skill handles capability negotiation automatically, selecting appropriate browser versions and OS combinations based on test requirements. It supports parallel test execution using TestNG or pytest-xdist, distributing test cases across available Grid nodes for maximum throughput. Session management includes automatic retry on node failures and intelligent load balancing.

Cloud provider integration handles authentication via environment variables, automatic tunnel setup for testing behind firewalls using BrowserStack Local or Sauce Connect, and test artifact collection including video recordings, network logs, and console output. Results are aggregated into unified reports with pass/fail status per browser-OS combination.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-cloud-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-cloud-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-cloud-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill selenium-grid-cloud-executor -a codex
```

### OpenClaw

```bash
clawhub install selenium-grid-cloud-executor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-cloud-executor/)
