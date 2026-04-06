---
title: "AWS IAM Privilege Escalation Audit"
slug: "aws-iam-privilege-escalation-audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
category: "Security &amp; Verification"
framework: "Claude Code"
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

Choose whichever method fits your setup:

1. Browse and install from Agent Skill Exchange.
2. Clone or download the upstream project manually.
3. Use the project package manager or installer if available.
4. Copy the skill into your local skills directory.
5. Follow the upstream documentation for environment-specific setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
