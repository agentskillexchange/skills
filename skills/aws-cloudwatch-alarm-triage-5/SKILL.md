---
name: "AWS CloudWatch Alarm Triage"
description: "Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudWatch Alarm Triage

Triages AWS CloudWatch alarms using boto3 CloudWatch.describe_alarms, CloudWatch Logs Insights queries, and AWS X-Ray trace analysis via the xray-sdk. Correlates alarm triggers with deployment events.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudwatch-alarm-triage-5
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-5 -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-5/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
