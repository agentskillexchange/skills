---
name: CloudTrail Anomaly Detection Agent
description: Analyzes AWS CloudTrail event logs via the Lookup Events API to detect
  anomalous IAM activity. Uses statistical baselining of API call patterns and flags
  unusual AssumeRole chains, console logins from new IPs, and privilege escalation
  attempts.
category: Security & Verification
framework: ChatGPT Agents
verification: security_reviewed
source: https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/
---
# CloudTrail Anomaly Detection Agent
Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudtrail-anomaly-detection-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cloudtrail-anomaly-detection-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
