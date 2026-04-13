---
title: "AWS IAM Privilege Escalation Audit"
slug: "aws-iam-privilege-escalation-audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&amp;CK TA0004 with remediation steps and least-privilege replacement policy JSON."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&amp;CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

Choose the install method that fits your setup:

1. Install from Agent Skill Exchange
2. Install with OpenClaw skill tools
3. Clone or copy the upstream project files
4. Add the skill to your local skills directory manually
5. Use the upstream package or repo install flow directly

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
