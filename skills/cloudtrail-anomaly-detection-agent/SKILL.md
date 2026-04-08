---
title: CloudTrail Anomaly Detection Agent
description: The CloudTrail Anomaly Detection Agent skill provides continuous security
  monitoring of AWS account activity by analyzing CloudTrail event logs through the
  Lookup Events API. It builds statistical baselines of normal API call patterns per
  IAM principal and detects deviations that may indicate compromised credentials or
  insider threats. Detection capabilities include unusual AssumeRole chain analysis
  where roles are chained through multiple accounts, console sign-in events from previously
  unseen IP addresses or geolocations, privilege escalation attempts through IAM policy
  modifications like AttachUserPolicy or PutRolePolicy, and resource enumeration patterns
  indicative of reconnaissance such as rapid List/Describe calls across services.
  The skill maintains per-principal behavioral profiles tracking typical API calls,
  source IPs, user agents, and active hours. Anomaly scoring uses z-score deviation
  from historical baselines with configurable sensitivity thresholds. It supports
  CloudTrail Lake queries for historical investigation, integration with AWS Organizations
  for multi-account monitoring, and structured alert output compatible with AWS Security
  Hub findings format. Time-based correlation groups related anomalous events into
  potential incident timelines.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/
category:
- Security &amp; Verification
framework:
- ChatGPT Agents
---

# CloudTrail Anomaly Detection Agent

The CloudTrail Anomaly Detection Agent skill provides continuous security monitoring of AWS account activity by analyzing CloudTrail event logs through the Lookup Events API. It builds statistical baselines of normal API call patterns per IAM principal and detects deviations that may indicate compromised credentials or insider threats. Detection capabilities include unusual AssumeRole chain analysis where roles are chained through multiple accounts, console sign-in events from previously unseen IP addresses or geolocations, privilege escalation attempts through IAM policy modifications like AttachUserPolicy or PutRolePolicy, and resource enumeration patterns indicative of reconnaissance such as rapid List/Describe calls across services. The skill maintains per-principal behavioral profiles tracking typical API calls, source IPs, user agents, and active hours. Anomaly scoring uses z-score deviation from historical baselines with configurable sensitivity thresholds. It supports CloudTrail Lake queries for historical investigation, integration with AWS Organizations for multi-account monitoring, and structured alert output compatible with AWS Security Hub findings format. Time-based correlation groups related anomalous events into potential incident timelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
