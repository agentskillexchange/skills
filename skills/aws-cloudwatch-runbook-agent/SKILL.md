---
name: "AWS CloudWatch Runbook Agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: "security_reviewed"
rating: 4.7
reviews: 81
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/aws-cloudwatch-runbook-agent/"
---

# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

## Installation

Install this skill across different agents:

### Any AI Agent (npx)
```bash
npx @anthropic/skills install aws-cloudwatch-runbook-agent
```

### Claude Code
```bash
claude skills install aws-cloudwatch-runbook-agent
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["aws-cloudwatch-runbook-agent"]
}
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-runbook-agent
```

### Codex
```bash
codex skills install aws-cloudwatch-runbook-agent
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.7/5 (81 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-runbook-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
