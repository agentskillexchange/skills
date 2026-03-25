---
name: "CodeClimate Maintainability Tracker"
description: "Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid."
category: "Code Quality & Review"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/"
tool_ecosystem:
  tool: "sendgrid"
  github_stars: 3054
  npm_weekly_downloads: 3287627
  github_repo: "sendgrid/sendgrid-nodejs"
  license: "MIT"
  maintained: true
---

# CodeClimate Maintainability Tracker

Tracks Code Climate maintainability scores over time using the Code Climate v1 API. Identifies technical debt hotspots, monitors churn-complexity coupling, and generates weekly maintainability digests via SendGrid.

## Overview

The CodeClimate Maintainability Tracker skill provides continuous technical debt monitoring by interfacing with the Code Climate v1 API. It fetches repository-level maintainability ratings, file-level complexity scores, and duplication metrics on a scheduled basis. The skill implements churn-complexity analysis by correlating Code Climate issue data with git log frequency, identifying files that are both highly complex and frequently modified — the true maintenance burden. It tracks maintainability grade changes across releases, flagging regressions before they compound. Generates formatted weekly digests with sparkline charts showing metric trends and sends them via SendGrid transactional email API. Supports badge generation for README files showing current maintainability grade. Can create GitHub Issues automatically for files that cross configured complexity thresholds. Integrates with Linear and Jira for technical debt backlog management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-tracker-7
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-tracker-7 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-tracker-7 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codeclimate-maintainability-tracker-7 -a codex
```

### OpenClaw

```bash
clawhub install codeclimate-maintainability-tracker-7
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codeclimate-maintainability-tracker-7/
