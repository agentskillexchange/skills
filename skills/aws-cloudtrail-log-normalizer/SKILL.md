---
title: AWS CloudTrail Log Normalizer
description: The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON
  events into the standardized Open Cybersecurity Schema Framework (OCSF) format for
  cross-platform security analytics. It maps AWS-specific event structures to OCSF
  activity classes including Authentication, API Activity, and Account Change events.
  The skill enriches each event by resolving AWS account IDs to friendly names, mapping
  IAM principal ARNs to human-readable identities, and geolocating source IP addresses
  using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations
  to MITRE ATT&CK technique IDs by querying the ATT&CK STIX/TAXII API (https://cti-taxii.mitre.org),
  enabling threat-informed detection engineering. Advanced features include session
  stitching that correlates AssumeRole chains to show complete identity traversal
  paths, anomaly detection for unusual API call patterns based on baseline profiling,
  and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy.
  The skill handles CloudTrail Insights events and can process both management and
  data events. Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with
  proper field mappings, and Sigma rule suggestions based on detected suspicious patterns.
  Supports processing from S3, CloudWatch Logs, or local file exports.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/
category:
- Security &amp; Verification
framework:
- Custom Agents
---

# AWS CloudTrail Log Normalizer

The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events. The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&CK technique IDs by querying the ATT&CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering. Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events. Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
