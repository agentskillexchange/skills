---
name: "Cron Job Manager"
description: "Use this skill when you need to list, create, modify, or debug cron jobs on a system or in a cloud scheduler (AWS EventBridge, GCP Cloud Scheduler). It validates cron expressions, explains schedules in plain language, and checks job execution history for failures."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cron-job-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Cron Job Manager

Use this skill when you need to list, create, modify, or debug cron jobs on a system or in a cloud scheduler (AWS EventBridge, GCP Cloud Scheduler). It validates cron expressions, explains schedules in plain language, and checks job execution history for failures.

## Overview

Use this skill when you need to list, create, modify, or debug cron jobs on a system or in a cloud scheduler (AWS EventBridge, GCP Cloud Scheduler). It validates cron expressions, explains schedules in plain language, and checks job execution history for failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cron-job-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cron-job-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cron-job-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cron-job-manager -a codex
```

### OpenClaw

```bash
clawhub install cron-job-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cron-job-manager/
