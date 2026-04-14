---
title: "AWS IAM Privilege Escalation Audit"
slug: "aws-iam-privilege-escalation-audit"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---
# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
