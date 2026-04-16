---
title: "Audit AWS IAM policies for risky permissions with Cloudsplaining"
description: "Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production."
verification: "listed"
source: "https://github.com/salesforce/cloudsplaining"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "salesforce/cloudsplaining"
  github_stars: 2202
---

# Audit AWS IAM policies for risky permissions with Cloudsplaining

Cloudsplaining is a clean security workflow for agents: inspect AWS IAM policies, identify risky actions and escalation paths, and produce findings before deploy or during access review. Invoke it when the operator job is IAM risk review, not when you simply need AWS to accept a policy document. The boundary is strong: this is preflight IAM analysis and remediation guidance, not a generic AWS SDK, cloud platform, or IAM product listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/)
