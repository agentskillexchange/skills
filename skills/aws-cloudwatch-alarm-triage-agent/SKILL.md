---
name: AWS CloudWatch Alarm Triage Agent
description: Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.7
reviews: 78
source: https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent/
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

## Overview

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-triage-agent
```

### Claude Code

```bash
claude mcp add aws-cloudwatch-alarm-triage-agent
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.7/5 (78 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudwatch-alarm-triage-agent/)
