---
name: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
category: "Security & Verification"
framework: "Claude Code"
verification: 
rating: 4.2
reviews: 49
creator: Chris Lee
creator_handle: chrislee
creator_verified: false
source: https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit/
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit -a cursor
```

### OpenClaw

```bash
clawhub install aws-iam-privilege-escalation-audit
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | Claude Code |
| Verification | Listed |
| Rating | 4.2/5 (49 reviews) |

## Creator

**Chris Lee**
- Profile: [@chrislee](https://agentskillexchange.com/browse-skills/?creator=chrislee)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
