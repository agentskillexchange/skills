---
name: "AWS CloudFormation Drift Detector"
description: "Detects infrastructure drift in AWS CloudFormation stacks using the AWS SDK boto3 detect_stack_drift API. Compares actual resource configurations against template definitions and generates remediation changesets."
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
verification: security_reviewed
rating: 4.3
reviews: 24
creator: "Sarah Chen"
creator_handle: "@sarahchen"
creator_verified: true
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector/"
---
# AWS CloudFormation Drift Detector

Detects infrastructure drift in AWS CloudFormation stacks using the AWS SDK boto3 detect_stack_drift API. Compares actual resource configurations against template definitions and generates remediation changesets.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector -a cursor
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Custom Agents |
| Verification | Security Reviewed |
| Rating | 4.3/5 (24 reviews) |

## Creator

**Sarah Chen** (Verified Creator ✓)
- Profile: [@sarahchen](https://agentskillexchange.com/browse-skills/?creator=sarahchen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-drift-detector/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
