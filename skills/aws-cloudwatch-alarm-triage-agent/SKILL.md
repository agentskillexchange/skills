---
title: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Alarm Triage Agent

The AWS CloudWatch Alarm Triage Agent automates incident response for CloudWatch alarm notifications. It uses the DescribeAlarms API to retrieve alarm configuration details including metric name, namespace, threshold, comparison operator, and evaluation periods, then queries GetMetricData to pull historical metric values for trend analysis.

The agent correlates alarm triggers with infrastructure changes by querying AWS CloudTrail via the LookupEvents API, identifying recent API calls that may have caused the alert (deployments, configuration changes, scaling events). It integrates with AWS Health API to check for ongoing AWS service issues that could explain metric anomalies.

For EC2-related alarms, it queries the DescribeInstances API for instance status checks and DescribeInstanceStatus for system/instance reachability. For RDS alarms, it uses DescribeDBInstances and DescribeEvents to check for maintenance windows, failovers, and storage issues. The agent calculates blast radius by mapping affected resources through AWS Resource Groups Tagging API and service dependency graphs defined in AWS Systems Manager OpsCenter. Remediation playbooks include AWS CLI commands for common fixes like scaling adjustments, security group corrections, and RDS parameter group modifications.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/)
