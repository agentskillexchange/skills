---
name: "AWS CloudWatch Alarm Triager"
description: "Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: verified_metadata
rating: 4.3
reviews: 25
creator: "Sarah O'Brien"
creator_handle: "@sarahcodes"
creator_verified: true
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/"
---
# AWS CloudWatch Alarm Triager

Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-triager
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a codex
```
## Details

| Property | Value |
|----------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | Verified |
| **Rating** | ⭐⭐⭐⭐ 4.3/5 (25 reviews) |

## Creator

**Sarah O'Brien** ✓

[View Profile](https://agentskillexchange.com/creator/sarahcodes/)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triager/)
- [Browse All Skills](https://agentskillexchange.com)
