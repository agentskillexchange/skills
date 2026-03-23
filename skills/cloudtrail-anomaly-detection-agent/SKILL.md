---
name: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: "✅ Verified"
rating: "4.4"
reviews: "69"
creator: "Sam Lee"
creator_handle: "@samlee_dev"
creator_verified: true
source: "https://agentskillexchange.com/skill/cloudtrail-anomaly-detection-agent/"
---

# CloudTrail Anomaly Detection Agent

Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install cloudtrail-anomaly-detection-agent
```

### Claude Code
```bash
claude mcp add cloudtrail-anomaly-detection-agent
```

### Cursor
Add to your `.cursor/skills.json`:
```json
{
  "cloudtrail-anomaly-detection-agent": {
    "source": "https://agentskillexchange.com/skill/cloudtrail-anomaly-detection-agent/"
  }
}
```

### OpenClaw
```bash
clawhub install cloudtrail-anomaly-detection-agent
```

### Codex
```bash
codex install cloudtrail-anomaly-detection-agent
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
