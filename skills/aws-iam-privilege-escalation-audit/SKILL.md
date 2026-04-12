---
title: "AWS IAM Privilege Escalation Audit"
slug: "aws-iam-privilege-escalation-audit"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
