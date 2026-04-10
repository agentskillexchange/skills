---
name: "AWS CloudTrail Log Normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
---

# AWS CloudTrail Log Normalizer

The AWS CloudTrail Log Normalizer skill transforms raw CloudTrail JSON events into the standardized Open Cybersecurity Schema Framework (OCSF) format for cross-platform security analytics. It maps AWS-specific event structures to OCSF activity classes including Authentication, API Activity, and Account Change events.
The skill enriches each event by resolving AWS account IDs to friendly names, mapping IAM principal ARNs to human-readable identities, and geolocating source IP addresses using MaxMind GeoIP2. Most importantly, it maps eventSource and eventName combinations to MITRE ATT&CK technique IDs by querying the ATT&CK STIX/TAXII API (https://cti-taxii.mitre.org), enabling threat-informed detection engineering.
Advanced features include session stitching that correlates AssumeRole chains to show complete identity traversal paths, anomaly detection for unusual API call patterns based on baseline profiling, and sensitive action highlighting for operations like iam:CreateAccessKey or s3:PutBucketPolicy. The skill handles CloudTrail Insights events and can process both management and data events.
Output formats include OCSF JSON, Elasticsearch-compatible NDJSON with proper field mappings, and Sigma rule suggestions based on detected suspicious patterns. Supports processing from S3, CloudWatch Logs, or local file exports.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
