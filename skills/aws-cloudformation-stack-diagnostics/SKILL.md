---
name: "AWS CloudFormation Stack Diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.9
reviews: 25
creator: Tom Anderson
creator_handle: tanderson
creator_verified: false
source: https://agentskillexchange.com/skill/aws-cloudformation-stack-diagnostics/
---

# AWS CloudFormation Stack Diagnostics

Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a cursor
```

### OpenClaw

```bash
clawhub install aws-cloudformation-stack-diagnostics
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.9/5 (25 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudformation-stack-diagnostics/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
