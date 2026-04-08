---
title: "AWS CloudWatch Runbook Agent"
slug: "aws-cloudwatch-runbook-agent"
verification: "security_reviewed"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/"
---

# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
