---
name: "Audit AWS IAM policies for risky permissions with Cloudsplaining"
slug: "audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining"
description: "Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production."
github_stars: 2202
verification: "security_reviewed"
source: "https://github.com/salesforce/cloudsplaining"
author: "Salesforce"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "salesforce/cloudsplaining"
  github_stars: 2202
---

# Audit AWS IAM policies for risky permissions with Cloudsplaining

Use Cloudsplaining when an agent needs to flag privilege-escalation paths and overbroad IAM permissions before an AWS policy change reaches production.

## Prerequisites

Python 3, AWS IAM policy JSON or account data, and Cloudsplaining.

## Installation

Use the upstream install or setup path that matches your environment:
- brew tap salesforce/cloudsplaining https://github.com/salesforce/cloudsplaining
- brew install cloudsplaining

Requirements and caveats from upstream:
- [![Python Version](https://img.shields.io/pypi/pyversions/cloudsplaining)](#)
- You must have the privileges to run [iam:GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html). The arn:aws:iam::aws:policy/SecurityAudit policy i...
- default-iam-results.json: This contains the raw JSON output of the report. You can use this data file for operating on the scan results for various purposes. For example, you could write a Python script that parses th...

Basic usage or getting-started notes:
- [Example report](https://opensource.salesforce.com/cloudsplaining/)
- Cloudsplaining also identifies IAM Roles that can be assumed by AWS Compute Services (such as EC2, ECS, EKS, or Lambda), as they can present greater risk than user-defined roles - especially if the AWS Compute service...
- You can also specify a custom exclusions file to filter out results that are False Positives for various reasons. For example, User Policies are permissive by design, whereas System roles are generally more restrictiv...

- Source: https://github.com/salesforce/cloudsplaining
- Extracted from upstream docs: https://raw.githubusercontent.com/salesforce/cloudsplaining/HEAD/README.md

## Documentation

- https://cloudsplaining.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-aws-iam-policies-for-risky-permissions-with-cloudsplaining/)
