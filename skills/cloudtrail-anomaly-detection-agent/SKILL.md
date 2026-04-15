---
title: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
verification: listed
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
---

# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/)
