---
name: "CodeClimate Maintainability Reporter"
description: "Queries the CodeClimate API to fetch maintainability ratings, technical debt estimates, and code smell trends. Surfaces files with the worst churn-to-complexity ratio and flags functions exceeding cognitive complexity thresholds. Outputs a prioritized refactor list."
category: "Code Quality & Review"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/codeclimate-maintainability-reporter/"
---

# CodeClimate Maintainability Reporter

Queries the CodeClimate API to fetch maintainability ratings, technical debt estimates, and code smell trends. Surfaces files with the worst churn-to-complexity ratio and flags functions exceeding cognitive complexity thresholds. Outputs a prioritized refactor list.

## Overview

Queries the CodeClimate API to fetch maintainability ratings, technical debt estimates, and code smell trends. Surfaces files with the worst churn-to-complexity ratio and flags functions exceeding cognitive complexity thresholds. Outputs a prioritized refactor list.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-reporter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-reporter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-reporter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-reporter -a codex
```

### OpenClaw

```bash
clawhub install codeclimate-maintainability-reporter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codeclimate-maintainability-reporter/
