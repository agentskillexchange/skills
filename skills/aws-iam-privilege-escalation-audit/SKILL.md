---
title: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
slug: "aws-iam-privilege-escalation-audit"
verification: "security_reviewed"
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
1. Install from the Agent Skill Exchange website
2. Clone or download the upstream source repository
3. Install via npm if the project is published there
4. Use the tool's package manager or release binaries
5. Copy the skill files into your local skills directory manually

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
