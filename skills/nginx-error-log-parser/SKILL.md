---
name: "Nginx Error Log Parser"
description: "Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to ide"
category: "Uncategorized"
framework: "Unknown"
verification: security_reviewed
rating: 4.9
reviews: 47
creator: "Community"
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-parser/"
---
# Nginx Error Log Parser

Parses nginx error.log and access.log files using pattern matching for 5xx status codes, upstream timeouts, and SSL handshake failures. Correlates error spikes with nginx -T configuration dumps to identify misconfigured proxy_pass and keepalive settings.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a cursor
```

### OpenClaw
```bash
clawhub install nginx-error-log-parser
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-parser -a codex
```
## Details

| | |
|---|---|
| **Category** | Uncategorized |
| **Framework** | Unknown |
| **Verification** | 🔵 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.9/5 (47 reviews) |

## Creator

**Community**

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/nginx-error-log-parser/)
- [Browse All Skills](https://agentskillexchange.com/)