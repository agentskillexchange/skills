---
name: "Sentry Error Triage Assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.4
reviews: 14
creator: "Omar Hassan"
creator_handle: "@ohassan"
creator_verified: true
source: "https://agentskillexchange.com/skills/sentry-error-triage-assistant/"
---
# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a cursor
```

### OpenClaw

```bash
clawhub install sentry-error-triage-assistant
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sentry-error-triage-assistant -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.4/5 (14 reviews) |

## Creator

**Omar Hassan** (Verified Creator ✓)
- Profile: [@ohassan](https://agentskillexchange.com/browse-skills/?creator=ohassan)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
