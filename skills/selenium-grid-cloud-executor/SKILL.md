---
title: "Selenium Grid Cloud Executor"
description: "Distributes browser test suites across Selenium Grid 4 nodes using RemoteWebDriver and the W3C WebDriver protocol. Supports parallel execution on BrowserStack and Sauce Labs with automatic capability negotiation."
verification: "security_reviewed"
source: "https://github.com/SeleniumHQ/selenium"
category:
  - "Browser Automation"
framework:
  - "Codex"
---

# Selenium Grid Cloud Executor

This skill enables distributed browser test execution across Selenium Grid 4 infrastructure or cloud providers like BrowserStack and Sauce Labs. It uses the RemoteWebDriver API with the W3C WebDriver protocol for cross-browser compatibility testing at scale.


The skill handles capability negotiation automatically, selecting appropriate browser versions and OS combinations based on test requirements. It supports parallel test execution using TestNG or pytest-xdist, distributing test cases across available Grid nodes for maximum throughput. Session management includes automatic retry on node failures and intelligent load balancing.


Cloud provider integration handles authentication via environment variables, automatic tunnel setup for testing behind firewalls using BrowserStack Local or Sauce Connect, and test artifact collection including video recordings, network logs, and console output. Results are aggregated into unified reports with pass/fail status per browser-OS combination.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/selenium-grid-cloud-executor/)
