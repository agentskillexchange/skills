---
name: "AWS CloudWatch Log Analyzer"
description: "Analyzes AWS CloudWatch Logs using the CloudWatch Logs API and Logs Insights query syntax. Identifies error patterns, calculates error rates, and generates metric filters from log data."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-log-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudWatch Log Analyzer

Analyzes AWS CloudWatch Logs using the CloudWatch Logs API and Logs Insights query syntax. Identifies error patterns, calculates error rates, and generates metric filters from log data.

## Overview

The AWS CloudWatch Log Analyzer skill provides intelligent analysis of application and infrastructure logs stored in Amazon CloudWatch. Using the CloudWatch Logs API, it retrieves log events from specified log groups and streams with time-range filtering. The Logs Insights query language is used for complex log analysis, supporting parse, filter, stats, and sort commands for pattern extraction. The skill identifies recurring error patterns by frequency analysis, correlates errors across multiple log groups for distributed system debugging, and calculates error rate trends over configurable time windows. Metric filter generation transforms log patterns into CloudWatch Metrics for dashboarding and alarming. The skill also manages log retention policies, analyzes log group storage costs, and can export log data to S3 for long-term analysis using the CreateExportTask API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-analyzer -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-log-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-log-analyzer/
