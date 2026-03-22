---
name: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using boto3 to correlate alarm state changes with CloudTrail events, EC2 instance metrics, and ELB target health. Generates root cause summaries linking alarms to recent deployments or scaling events."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "✅ Verified"
security: "✅ Reviewed"
rating: "4.9"
reviews: "25"
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: true
source: "https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-4/"
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using boto3 to correlate alarm state changes with CloudTrail events, EC2 instance metrics, and ELB target health. Generates root cause summaries linking alarms to recent deployments or scaling events.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install aws-cloudwatch-alarm-triage-agent-4
```

### Claude Code
```bash
claude skills add aws-cloudwatch-alarm-triage-agent-4
```

### Cursor
Add to your `.cursor/skills` configuration:
```json
{
  "skills": ["aws-cloudwatch-alarm-triage-agent-4"]
}
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-triage-agent-4
```

### Codex
```bash
codex skills add aws-cloudwatch-alarm-triage-agent-4
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
[View Profile on ASE](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-4/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-4/) • [Browse All Skills](https://agentskillexchange.com)