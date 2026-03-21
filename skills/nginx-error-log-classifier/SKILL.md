---
name: "Nginx Error Log Classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend ..."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: "security_reviewed"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/nginx-error-log-classifier/"
---

# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/skills install nginx-error-log-classifier
```

### Claude Code
```bash
claude mcp add nginx-error-log-classifier
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "nginx-error-log-classifier": {
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install nginx-error-log-classifier
```

### Codex
```bash
codex install nginx-error-log-classifier
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | security_reviewed |
| **Rating** | 0 (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/nginx-error-log-classifier/)
- [Browse All Skills](https://agentskillexchange.com/)
