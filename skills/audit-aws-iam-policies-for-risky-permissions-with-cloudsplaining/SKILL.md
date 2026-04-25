---
title: "Audit AWS IAM policies for risky permissions with Cloudsplaining"
description: "Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production."
verification: "listed"
source: "https://github.com/salesforce/cloudsplaining"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "salesforce/cloudsplaining"
  github_stars: 2202
---

# Audit AWS IAM policies for risky permissions with Cloudsplaining

Cloudsplaining is a clean security workflow for agents: inspect AWS IAM policies, identify risky actions and escalation paths, and produce findings before deploy or during access review. Invoke it when the operator job is IAM risk review, not when you simply need AWS to accept a policy document. The boundary is strong: this is preflight IAM analysis and remediation guidance, not a generic AWS SDK, cloud platform, or IAM product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/)
