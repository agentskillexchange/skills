---
name: "AWS CloudWatch Runbook Agent"
slug: "aws-cloudwatch-runbook-agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
github_stars: 3607
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
