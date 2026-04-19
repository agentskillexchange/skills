---
title: "AWS CloudWatch Log Analyzer"
description: "The AWS CloudWatch Log Analyzer skill provides intelligent analysis of application and infrastructure logs stored in Amazon CloudWatch. Using the CloudWatch Logs API, it retrieves log events from specified log groups and streams with time-range filtering. The Logs Insights query language is used for complex log analysis, supporting parse, filter, stats, and sort commands for pattern extraction. The skill identifies recurring error patterns by frequency analysis, correlates errors across multiple log groups for distributed system debugging, and calculates error rate trends over configurable time windows. Metric filter generation transforms log patterns into CloudWatch Metrics for dashboarding and alarming. The skill also manages log retention policies, analyzes log group storage costs, and can export log data to S3 for long-term analysis using the CreateExportTask API."
source: "https://github.com/aws/aws-sdk-js-v3"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Log Analyzer

The AWS CloudWatch Log Analyzer skill provides intelligent analysis of application and infrastructure logs stored in Amazon CloudWatch. Using the CloudWatch Logs API, it retrieves log events from specified log groups and streams with time-range filtering. The Logs Insights query language is used for complex log analysis, supporting parse, filter, stats, and sort commands for pattern extraction. The skill identifies recurring error patterns by frequency analysis, correlates errors across multiple log groups for distributed system debugging, and calculates error rate trends over configurable time windows. Metric filter generation transforms log patterns into CloudWatch Metrics for dashboarding and alarming. The skill also manages log retention policies, analyzes log group storage costs, and can export log data to S3 for long-term analysis using the CreateExportTask API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-analyzer/)
