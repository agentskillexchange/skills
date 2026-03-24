---
name: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
category: "Security & Verification"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
