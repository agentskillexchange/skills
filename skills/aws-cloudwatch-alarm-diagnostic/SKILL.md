---
name: "AWS CloudWatch Alarm Diagnostic"
description: "Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.3
reviews: 81
creator: "Nathan Brooks"
creator_handle: "@nbrooks"
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/"
---
# AWS CloudWatch Alarm Diagnostic

Diagnoses firing AWS CloudWatch alarms by querying CloudWatch Metrics, alarm history, and related AWS Config resource snapshots via the AWS SDK. Correlates metric anomalies with recent infrastructure changes to suggest root cause hypotheses. Outputs a structured incident summary with remediation options.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | 4.3/5 (81 reviews) |

## Creator

**Nathan Brooks**
- Profile: [@nbrooks](https://agentskillexchange.com/browse-skills/?creator=nbrooks)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-diagnostic/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
