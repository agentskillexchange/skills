---
name: "CloudTrail Anomaly Detection Agent"
slug: "cloudtrail-anomaly-detection-agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: "listed"
source: "https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html"
category: "Security & Verification"
framework: "ChatGPT Agents"
---

# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

Requirements and caveats from upstream:
- AWS SDK for Python

Basic usage or getting-started notes:
- LookupEvents returns recent Insights events for trails that enable Insights. To view Insights events for an event data store, you can run queries on your
- category are not returned in the response. For example, if you do not specify
- example, if the original call specified an AttributeKey of 'Username' with a value of

- Source: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
