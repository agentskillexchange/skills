---
title: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/"
category:
  - "Runbooks &amp; Diagnostics"
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/)
