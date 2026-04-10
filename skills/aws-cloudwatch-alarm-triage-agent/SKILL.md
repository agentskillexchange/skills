---
name: AWS CloudWatch Alarm Triage Agent
description: Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API,
  GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause
  correlation. Prioritizes alerts by blast radius and provides remediation playbooks.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---
# AWS CloudWatch Alarm Triage Agent

The AWS CloudWatch Alarm Triage Agent automates incident response for CloudWatch alarm notifications. It uses the DescribeAlarms API to retrieve alarm configuration details including metric name, namespace, threshold, comparison operator, and evaluation periods, then queries GetMetricData to pull historical metric values for trend analysis.
The agent correlates alarm triggers with infrastructure changes by querying AWS CloudTrail via the LookupEvents API, identifying recent API calls that may have caused the alert (deployments, configuration changes, scaling events). It integrates with AWS Health API to check for ongoing AWS service issues that could explain metric anomalies.
For EC2-related alarms, it queries the DescribeInstances API for instance status checks and DescribeInstanceStatus for system/instance reachability. For RDS alarms, it uses DescribeDBInstances and DescribeEvents to check for maintenance windows, failovers, and storage issues. The agent calculates blast radius by mapping affected resources through AWS Resource Groups Tagging API and service dependency graphs defined in AWS Systems Manager OpsCenter. Remediation playbooks include AWS CLI commands for common fixes like scaling adjustments, security group corrections, and RDS parameter group modifications.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/)
