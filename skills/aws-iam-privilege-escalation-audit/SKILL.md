---
name: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
category: "Security & Verification"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Overview

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-iam-privilege-escalation-audit -a codex
```

### OpenClaw

```bash
clawhub install aws-iam-privilege-escalation-audit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/
