---
title: "AWS CloudTrail Log Normalizer"
slug: "aws-cloudtrail-log-normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudTrail Log Normalizer

Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
