---
title: "Audit AWS IAM policies for risky permissions with Cloudsplaining"
description: "Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production."
verification: "security_reviewed"
source: "https://github.com/salesforce/cloudsplaining"
author: "Salesforce"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "salesforce/cloudsplaining"
  github_stars: 2202
---

# Audit AWS IAM policies for risky permissions with Cloudsplaining

Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production.

## Prerequisites

Python 3, AWS IAM policy JSON or account data, and Cloudsplaining.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install cloudsplaining`, export or collect the IAM policies you want to review, then run Cloudsplaining reports as part of access review or deployment checks.
```

## Documentation

- https://cloudsplaining.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/)
