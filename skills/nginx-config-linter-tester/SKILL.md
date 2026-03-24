---
name: "Nginx Config Linter and Tester"
description: "Validates nginx.conf files using the gixy static analyzer and crossplane parser library. Tests configuration for security misconfigs, HTTP header issues, and performs dry-run validation via nginx -t subprocess invocation."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.5
reviews: 75
creator: "Leo Park"
creator_handle: "@leopark"
creator_verified: true
source: "https://agentskillexchange.com/skills/nginx-config-linter-tester/"
---
# Nginx Config Linter and Tester

Validates nginx.conf files using the gixy static analyzer and crossplane parser library. Tests configuration for security misconfigs, HTTP header issues, and performs dry-run validation via nginx -t subprocess invocation.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a cursor
```

### OpenClaw

```bash
clawhub install nginx-config-linter-tester
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nginx-config-linter-tester -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.5/5 (75 reviews) |

## Creator

**Leo Park** (Verified Creator ✓)
- Profile: [@leopark](https://agentskillexchange.com/browse-skills/?creator=leopark)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/nginx-config-linter-tester/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
