---
name: AWS IAM Privilege Escalation Audit
description: Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.
category: Security &amp; Verification
framework: Any Agent
verification: listed
rating: 4.2
reviews: 49
source: https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit/
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Overview

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit
```

### OpenClaw

```bash
clawhub install aws-iam-privilege-escalation-audit
```

### Claude Code

```bash
claude mcp add aws-iam-privilege-escalation-audit
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.2/5 (49 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit/)
