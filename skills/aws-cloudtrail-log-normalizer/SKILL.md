---
name: "AWS CloudTrail Log Normalizer"
description: "Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API."
category: "Security & Verification"
framework: "Custom Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# AWS CloudTrail Log Normalizer

Normalizes and enriches AWS CloudTrail JSON logs into OCSF (Open Cybersecurity Schema Framework) format. Maps eventSource/eventName pairs to MITRE ATT&CK technique IDs using the MITRE ATT&CK STIX API.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a cursor
```

### OpenClaw
```bash
clawhub install aws-cloudtrail-log-normalizer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill aws-cloudtrail-log-normalizer -a codex
```

## Details

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | Custom Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudtrail-log-normalizer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
