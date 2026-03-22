---
name: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms by querying the CloudWatch GetMetricData API and correlating with AWS Health events. Uses AWS X-Ray trace analysis and CloudTrail lookup-events to reconstruct incident timelines for SNS-triggered on-call escalations."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: "✅ Verified"
rating: "4.9"
reviews: "58"
creator: "Yuki Tanaka"
creator_handle: "@yukitanaka"
creator_verified: "true"
source: "https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-3/"
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms by querying the CloudWatch GetMetricData API and correlating with AWS Health events. Uses AWS X-Ray trace analysis and CloudTrail lookup-events to reconstruct incident timelines for SNS-triggered on-call escalations.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install aws-cloudwatch-alarm-triage-agent-3
```

### Claude Code
```bash
claude mcp add aws-cloudwatch-alarm-triage-agent-3
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["aws-cloudwatch-alarm-triage-agent-3"]
}
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-triage-agent-3
```

### Codex
```bash
codex install aws-cloudwatch-alarm-triage-agent-3
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | ✅ Verified 🔒 Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.9/5 (58 reviews) |

## Creator

**Yuki Tanaka** ✅
Handle: `@yukitanaka`
[View Profile on ASE](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-3/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent-3/) · [Browse All Skills](https://agentskillexchange.com/skills/)