---
name: "AWS IAM Privilege Escalation Audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
category: "Security &amp; Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/"
---
# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

AWS IAM Privilege Escalation Audit is built around Amazon Web Services cloud APIs. The underlying ecosystem is represented by aws/aws-sdk-js-v3 (3,594+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like AWS SDK, IAM, STS, S3, Lambda, CloudWatch, DynamoDB, EC2 and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to aws so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON. The implementation typically relies on AWS SDK, IAM, STS, S3, Lambda, CloudWatch, DynamoDB, EC2, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses AWS SDK, IAM, STS, S3, Lambda, CloudWatch, DynamoDB, EC2 instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as cloud automation, identity, serverless jobs, storage, and audit pipelines.

In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include cloud automation, identity, serverless jobs, storage, and audit pipelines. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
