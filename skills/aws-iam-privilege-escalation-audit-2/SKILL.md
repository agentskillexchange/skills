---
name: AWS IAM Privilege Escalation Audit
description: Uses boto3 and AWS IAM Access Analyzer to enumerate roles, policies, and users, flagging permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement JSON.
category: Security &amp; Verification
framework: Any Agent
verification: security_reviewed
rating: 4.0
reviews: 16
source: https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit-2/
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and AWS IAM Access Analyzer to enumerate roles, policies, and users, flagging permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement JSON.

## Overview

Uses boto3 and AWS IAM Access Analyzer to enumerate roles, policies, and users, flagging permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement JSON.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit-2
```

### OpenClaw

```bash
clawhub install aws-iam-privilege-escalation-audit-2
```

### Claude Code

```bash
claude mcp add aws-iam-privilege-escalation-audit-2
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit-2/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.0/5 (16 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit-2/)
