---
name: "CloudTrail Anomaly Detection Agent"
description: "Analyzes AWS CloudTrail event logs via the Lookup Events API to detect anomalous IAM activity. Uses statistical baselining of API call patterns and flags unusual AssumeRole chains, console logins from new IPs, and privilege escalation attempts."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
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

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/cloudtrail-anomaly-detection-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
