---
title: "AWS CloudTrail Log Normalizer"
description: "The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events. The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&#038;CK technique IDs by querying the ATT&#038;CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering. Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events. Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports."
source: "https://github.com/aws/aws-sdk-js-v3"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudTrail Log Normalizer

The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events. The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&#038;CK technique IDs by querying the ATT&#038;CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering. Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events. Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
