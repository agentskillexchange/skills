---
title: "Audit cloud accounts for security misconfigurations with Prowler"
slug: "audit-cloud-accounts-for-security-misconfigurations-with-prowler"
description: "Run targeted AWS, Azure, or GCP security and compliance audits when an agent needs actionable cloud findings instead of a generic cloud-security platform overview."
github_stars: 13635
verification: "security_reviewed"
source: "https://github.com/prowler-cloud/prowler"
author: "Prowler Cloud"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "prowler-cloud/prowler"
  github_stars: 13635
---

# Audit cloud accounts for security misconfigurations with Prowler

Run targeted AWS, Azure, or GCP security and compliance audits when an agent needs actionable cloud findings instead of a generic cloud-security platform overview.

## Prerequisites

Python or Docker runtime, cloud account credentials, optional AWS CLI or equivalent cloud auth setup

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Prowler with pipx, pip, Homebrew, or Docker, authenticate to the target cloud account, then run the relevant provider checks such as `prowler aws`, `prowler azure`, or `prowler gcp` and review the generated findings report.
```

## Documentation

- https://github.com/prowler-cloud/prowler#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-cloud-accounts-for-security-misconfigurations-with-prowler/)
