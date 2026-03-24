---
name: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using boto3 to correlate alarm state changes with CloudTrail events, EC2 instance metrics, and ELB target health. Generates root cause summaries linking alarms to recent deployments or scaling events."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.9
reviews: 25
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent-4/"
security: "✅ Reviewed"
---
# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using boto3 to correlate alarm state changes with CloudTrail events, EC2 instance metrics, and ELB target health. Generates root cause summaries linking alarms to recent deployments or scaling events.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent-4
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent-4 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent-4 -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-triage-agent-4
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent-4 -a codex
```
## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | ✅ Verified |
| **Security** | ✅ Reviewed |
| **Rating** | ⭐ 4.9 (25 reviews) |

## Creator

**Yuki Tanaka** ✅
Handle: `@yukitanaka`
[View Profile on ASE](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent-4/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent-4/) • [Browse All Skills](https://agentskillexchange.com)