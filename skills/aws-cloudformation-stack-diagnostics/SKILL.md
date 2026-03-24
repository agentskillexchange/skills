---
name: "AWS CloudFormation Stack Diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/"
tool_ecosystem:
  tool: "cloudformation"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudFormation Stack Diagnostics

Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [cloudformation](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
