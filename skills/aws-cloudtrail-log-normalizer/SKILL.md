---
name: "AWS CloudTrail Log Normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
category: "Security & Verification"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudTrail Log Normalizer

Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API.

## Overview

The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events.

The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&CK technique IDs by querying the ATT&CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering.

Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events.

Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudtrail-log-normalizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/
