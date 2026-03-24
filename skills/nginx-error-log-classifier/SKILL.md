---
name: "Nginx Error Log Classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend ..."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-classifier/"
---
# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a cursor
```

### OpenClaw
```bash
clawhub install nginx-error-log-classifier
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a codex
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

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/)
- [Browse All Skills](https://agentskillexchange.com/)
