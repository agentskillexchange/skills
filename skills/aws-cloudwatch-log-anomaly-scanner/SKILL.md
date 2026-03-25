---
name: "AWS CloudWatch Log Anomaly Scanner"
description: "Scans AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection API. Identifies unusual error patterns, latency spikes, and log volume anomalies across log groups."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudWatch Log Anomaly Scanner

Scans AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection API. Identifies unusual error patterns, latency spikes, and log volume anomalies across log groups.

## Overview

The AWS CloudWatch Log Anomaly Scanner skill uses the CloudWatch Logs Insights API (StartQuery/GetQueryResults) to run analytical queries across multiple log groups simultaneously. It constructs dynamic Insights queries that aggregate error frequencies, parse structured JSON log fields, and compute percentile latency distributions. The skill leverages the CloudWatch Anomaly Detection API to establish baseline patterns for error rates and log volumes, then flags deviations exceeding configurable sigma thresholds. Cross-log-group correlation identifies cascading failures by matching request IDs and trace headers across Lambda, ECS, and API Gateway log groups. The skill integrates with the X-Ray API (GetTraceSummaries) to correlate log anomalies with distributed trace data. Export functionality uses the CreateExportTask API to archive anomalous log windows to S3 for forensic analysis. Alert rules can be generated as CloudWatch Metric Filter definitions with proper namespace and dimension configurations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-scanner -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-log-anomaly-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-scanner/
