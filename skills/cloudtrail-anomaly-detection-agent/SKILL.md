---
title: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---

# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

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
