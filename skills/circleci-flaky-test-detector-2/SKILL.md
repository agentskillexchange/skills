---
name: CircleCI Flaky Test Detector
description: Queries CircleCI Insights API to identify test cases that flip between
  pass and fail across recent runs. Produces a ranked list by failure rate with quarantine
  strategies for Jest, pytest, RSpec, and JUnit.
category: CI/CD Integrations
framework: MCP
verification: security_reviewed
source: https://github.com/circleci/circleci-docs
tool_ecosystem:
  github_repo: circleci/circleci-docs
  github_stars: 843
  tool: circleci-docs
  maintained: true
---
# CircleCI Flaky Test Detector
Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-flaky-test-detector-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-flaky-test-detector-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-flaky-test-detector-2/)
