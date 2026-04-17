---
title: "Audit AWS IAM policies for risky permissions with Cloudsplaining"
description: "Cloudsplaining is a clean security workflow for agents: inspect AWS IAM policies, identify risky actions and escalation paths, and produce findings before deploy or during access review. Invoke it when the operator job is IAM risk review, not when you simply need AWS to accept a policy document. The boundary is strong: this is preflight IAM analysis and remediation guidance, not a generic AWS SDK, cloud platform, or IAM product listing."
verification: listed
source: "https://github.com/salesforce/cloudsplaining"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "salesforce/cloudsplaining"
  github_stars: 2202
---

# Audit AWS IAM policies for risky permissions with Cloudsplaining

Cloudsplaining is a clean security workflow for agents: inspect AWS IAM policies, identify risky actions and escalation paths, and produce findings before deploy or during access review. Invoke it when the operator job is IAM risk review, not when you simply need AWS to accept a policy document. The boundary is strong: this is preflight IAM analysis and remediation guidance, not a generic AWS SDK, cloud platform, or IAM product listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/)
