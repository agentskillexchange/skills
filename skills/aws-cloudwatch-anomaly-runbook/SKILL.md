---
name: "AWS CloudWatch Anomaly Runbook"
description: "Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudWatch Anomaly Runbook

Executes structured diagnostic runbooks when CloudWatch Anomaly Detection triggers alarms. Uses the AWS SDK CloudWatch client (GetMetricData, DescribeAlarms) to gather context and suggest remediations.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-anomaly-runbook
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-runbook -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
