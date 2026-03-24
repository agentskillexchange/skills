---
name: "AWS CloudFormation Drift Detector"
description: "Detects and reports configuration drift in AWS CloudFormation stacks using the detect-stack-drift and describe-stack-resource-drifts APIs via boto3. Generates remediation templates using cfn-flip for YAML/JSON conversion."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 4.5
reviews: 86
creator: "Nathan Brooks"
creator_handle: "@nbrooks"
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-2/"
---
# AWS CloudFormation Drift Detector

Detects and reports configuration drift in AWS CloudFormation stacks using the detect-stack-drift and describe-stack-resource-drifts APIs via boto3. Generates remediation templates using cfn-flip for YAML/JSON conversion.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-2 -a cursor
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector-2
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-2 -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Security Reviewed |
| Rating | 4.5/5 (86 reviews) |

## Creator

**Nathan Brooks**
- Profile: [@nbrooks](https://agentskillexchange.com/browse-skills/?creator=nbrooks)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/aws-cloudformation-drift-detector-2/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
