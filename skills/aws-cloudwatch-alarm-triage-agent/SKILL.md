---
name: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.7
reviews: 78
creator: "Rachel Green"
creator_handle: "@rachelgreen"
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/"
---
# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a cursor
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-triage-agent
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.7/5 (78 reviews) |

## Creator

**Rachel Green**
- Profile: [@rachelgreen](https://agentskillexchange.com/browse-skills/?creator=rachelgreen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
