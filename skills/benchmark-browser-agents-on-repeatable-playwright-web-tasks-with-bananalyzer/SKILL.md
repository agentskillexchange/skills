---
name: "Benchmark browser agents on repeatable Playwright web tasks with Bananalyzer"
slug: "benchmark-browser-agents-on-repeatable-playwright-web-tasks-with-bananalyzer"
description: "Run a repeatable evaluation suite for browser agents against static web task snapshots instead of judging them from demos or one-off tests."
github_stars: 327
verification: "listed"
source: "https://github.com/reworkd/bananalyzer"
author: "Reworkd"
publisher_type: "organization"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "reworkd/bananalyzer"
  github_stars: 327
---

# Benchmark browser agents on repeatable Playwright web tasks with Bananalyzer

Run a repeatable evaluation suite for browser agents against static web task snapshots instead of judging them from demos or one-off tests.

## Prerequisites

Python environment, Playwright browser runtime, pytest-based test execution, a custom AgentRunner implementation, example web task snapshots

## Installation

Requirements and caveats from upstream:
- <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
- individual website. For an agent to best generalize, we require building a diverse dataset of websites across
- In the future we will support more complex evaluation methods and examples that require multiple steps to complete. The

Basic usage or getting-started notes:
- Banana-lyzer is a CLI tool that runs a set of evaluations against a set of example websites.
- The CLI tool will sequentially run examples against a user defined agent by dynamically constructing a pytest test suite
- AgentRunner exposes the example, and a playwright browser context to use.

- Source: https://github.com/reworkd/bananalyzer
- Extracted from upstream docs: https://raw.githubusercontent.com/reworkd/bananalyzer/HEAD/README.md

## Documentation

- https://github.com/reworkd/bananalyzer

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-browser-agents-on-repeatable-playwright-web-tasks-with-bananalyzer/)
