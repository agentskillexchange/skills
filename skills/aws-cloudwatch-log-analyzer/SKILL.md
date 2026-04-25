---
title: "AWS CloudWatch Log Analyzer"
description: "Analyzes AWS CloudWatch Logs using the CloudWatch Logs API and Logs Insights query syntax. Identifies error patterns, calculates error rates, and generates metric filters from log data."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Log Analyzer

The AWS CloudWatch Log Analyzer skill provides intelligent analysis of application and infrastructure logs stored in Amazon CloudWatch. Using the CloudWatch Logs API, it retrieves log events from specified log groups and streams with time-range filtering. The Logs Insights query language is used for complex log analysis, supporting parse, filter, stats, and sort commands for pattern extraction. The skill identifies recurring error patterns by frequency analysis, correlates errors across multiple log groups for distributed system debugging, and calculates error rate trends over configurable time windows. Metric filter generation transforms log patterns into CloudWatch Metrics for dashboarding and alarming. The skill also manages log retention policies, analyzes log group storage costs, and can export log data to S3 for long-term analysis using the CreateExportTask API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudwatch-log-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-log-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudwatch-log-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-analyzer/)
