---
title: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
---

# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
