---
name: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and AWS IAM Access Analyzer to enumerate roles, policies, and users, flagging permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement JSON."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
rating: 4.0
reviews: 16
creator: Omar Hassan
creator_handle: ohassan
creator_verified: true
source: https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit-2/
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and AWS IAM Access Analyzer to enumerate roles, policies, and users, flagging permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement JSON.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit-2 -a cursor
```

### OpenClaw

```bash
clawhub install aws-iam-privilege-escalation-audit-2
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit-2 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.0/5 (16 reviews) |

## Creator

**Omar Hassan** (Verified Creator ✓)
- Profile: [@ohassan](https://agentskillexchange.com/browse-skills/?creator=ohassan)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-iam-privilege-escalation-audit-2/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
