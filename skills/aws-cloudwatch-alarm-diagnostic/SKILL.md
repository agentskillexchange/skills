---
name: "AWS CloudWatch Alarm Diagnostic"
description: "Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudWatch Alarm Diagnostic

Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-diagnostic
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-diagnostic -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
