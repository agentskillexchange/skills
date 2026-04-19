---
title: "CloudTrail Anomaly Detection Agent"
description: "The CloudTrail Anomaly Detection Agent skill provides continuous security monitoring of AWS account activity by analyzing CloudTrail event logs through the Lookup Events API. It builds statistical baselines of normal API call patterns per IAM principal and detects deviations that may indicate compromised credentials or insider threats. Detection capabilities include unusual AssumeRole chain analysis where roles are chained through multiple accounts, console sign-in events from previously unseen IP addresses or geolocations, privilege escalation attempts through IAM policy modifications like AttachUserPolicy or PutRolePolicy, and resource enumeration patterns indicative of reconnaissance such as rapid List/Describe calls across services. The skill maintains per-principal behavioral profiles tracking typical API calls, source IPs, user agents, and active hours. Anomaly scoring uses z-score deviation from historical baselines with configurable sensitivity thresholds. It supports CloudTrail Lake queries for historical investigation, integration with AWS Organizations for multi-account monitoring, and structured alert output compatible with AWS Security Hub findings format. Time-based correlation groups related anomalous events into potential incident timelines."
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
---

# CloudTrail Anomaly Detection Agent

The CloudTrail Anomaly Detection Agent skill provides continuous security monitoring of AWS account activity by analyzing CloudTrail event logs through the Lookup Events API. It builds statistical baselines of normal API call patterns per IAM principal and detects deviations that may indicate compromised credentials or insider threats. Detection capabilities include unusual AssumeRole chain analysis where roles are chained through multiple accounts, console sign-in events from previously unseen IP addresses or geolocations, privilege escalation attempts through IAM policy modifications like AttachUserPolicy or PutRolePolicy, and resource enumeration patterns indicative of reconnaissance such as rapid List/Describe calls across services. The skill maintains per-principal behavioral profiles tracking typical API calls, source IPs, user agents, and active hours. Anomaly scoring uses z-score deviation from historical baselines with configurable sensitivity thresholds. It supports CloudTrail Lake queries for historical investigation, integration with AWS Organizations for multi-account monitoring, and structured alert output compatible with AWS Security Hub findings format. Time-based correlation groups related anomalous events into potential incident timelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
