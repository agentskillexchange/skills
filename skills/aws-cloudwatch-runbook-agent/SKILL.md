---
name: "AWS CloudWatch Runbook Agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-runbook-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
