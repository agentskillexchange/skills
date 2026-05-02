---
title: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---

# CloudTrail Anomaly Detection Agent

The CloudTrail Anomaly Detection Agent skill provides continuous security monitoring of AWS account activity by analyzing CloudTrail event logs through the Lookup Events API. It builds statistical baselines of normal API call patterns per IAM principal and detects deviations that may indicate compromised credentials or insider threats.

Detection capabilities include unusual AssumeRole chain analysis where roles are chained through multiple accounts, console sign-in events from previously unseen IP addresses or geolocations, privilege escalation attempts through IAM policy modifications like AttachUserPolicy or PutRolePolicy, and resource enumeration patterns indicative of reconnaissance such as rapid List/Describe calls across services.

The skill maintains per-principal behavioral profiles tracking typical API calls, source IPs, user agents, and active hours. Anomaly scoring uses z-score deviation from historical baselines with configurable sensitivity thresholds. It supports CloudTrail Lake queries for historical investigation, integration with AWS Organizations for multi-account monitoring, and structured alert output compatible with AWS Security Hub findings format. Time-based correlation groups related anomalous events into potential incident timelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudtrail-anomaly-detection-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudtrail-anomaly-detection-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
