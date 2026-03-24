---
name: "Sentry Error Triage Assistant"
description: "Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sentry-error-triage-assistant/"
tool_ecosystem:
  tool: "sentry"
  github_stars: 43434
  npm_weekly_downloads: 16379655
  github_repo: "getsentry/sentry"
  license: "NOASSERTION"
  maintained: true
---

# Sentry Error Triage Assistant

Triages application errors using the Sentry Web API (/api/0/issues/) and Sentry SDK breadcrumb data. Groups issues by stack trace similarity using Sentry fingerprinting rules and queries release health via the /api/0/organizations/{org}/releases/ endpoint.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [sentry](https://github.com/getsentry/sentry) — ⭐ 43.4k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-error-triage-assistant/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
