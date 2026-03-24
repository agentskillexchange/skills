---
name: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.4
reviews: 69
creator: "Sam Lee"
creator_handle: "@samlee_dev"
creator_verified: true
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
---
# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill cloudtrail-anomaly-detection-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill cloudtrail-anomaly-detection-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill cloudtrail-anomaly-detection-agent -a cursor
```

### OpenClaw
```bash
clawhub install cloudtrail-anomaly-detection-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill cloudtrail-anomaly-detection-agent -a codex
```
## Details

| Field | Value |
|-------|-------|
| **Category** | Security & Verification |
| **Framework** | ChatGPT Agents |
| **Verification** | ✅ Verified |
| **Security** | ✅ Reviewed |
| **Rating** | ⭐ 4.4/5.0 (69 reviews) |

## Creator

**Sam Lee** ✅
- Handle: @samlee_dev
- [View Profile](https://agentskillexchange.com/creator/samlee_dev/)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/cloudtrail-anomaly-detection-agent/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
