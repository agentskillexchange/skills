---
name: "CircleCI Flaky Test Detector"
description: "Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-flaky-test-detector-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Flaky Test Detector

Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit.

## Overview

Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-flaky-test-detector-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-flaky-test-detector-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-flaky-test-detector-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-flaky-test-detector-2 -a codex
```

### OpenClaw

```bash
clawhub install circleci-flaky-test-detector-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-flaky-test-detector-2/
