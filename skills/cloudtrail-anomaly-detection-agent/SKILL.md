---
title: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---
# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

You can install this skill in a few common ways:

1. Browse and install from Agent Skill Exchange in the UI if your client supports it.
2. Install from a local skill folder by copying it into your skills directory.
3. Add it as a git submodule or vendor it into your shared skills repo.
4. Fetch it with your preferred skill or package workflow if the upstream project publishes one.
5. Follow the upstream project documentation for manual setup and dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
