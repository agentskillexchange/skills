---
name: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: "Security Reviewed ✓"
rating: "4.9"
reviews: "81"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/aws-cloudwatch-anomaly-runbook/"
---

# AWS CloudWatch Anomaly Runbook

Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations.

## Installation

**Any Agent (npx):**
```bash
npx @anthropic/skills install aws-cloudwatch-anomaly-runbook
```

**Claude Code:**
```bash
claude mcp add aws-cloudwatch-anomaly-runbook
```

**Cursor:**
Add to `.cursor/skills.json`:
```json
{
  "aws-cloudwatch-anomaly-runbook": "latest"
}
```

**OpenClaw:**
```bash
clawhub install aws-cloudwatch-anomaly-runbook
```

**Codex:**
```bash
codex install aws-cloudwatch-anomaly-runbook
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | Security Reviewed ✓ |
| **Rating** | ⭐ 4.9/5 (81 reviews) |

## Creator

**Community**


---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-anomaly-runbook/) • [Browse All Skills](https://agentskillexchange.com/)