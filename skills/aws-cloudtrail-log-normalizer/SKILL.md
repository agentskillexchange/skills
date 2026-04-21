---
title: "AWS CloudTrail Log Normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudTrail Log Normalizer

Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudtrail-log-normalizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudtrail-log-normalizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/)
