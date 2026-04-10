---
title: "AWS CloudTrail Log Normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
slug: "aws-cloudtrail-log-normalizer"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/"
---

# AWS CloudTrail Log Normalizer

Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install aws-cloudtrail-log-normalizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events.
The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&CK technique IDs by querying the ATT&CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering.
Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events.
Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
