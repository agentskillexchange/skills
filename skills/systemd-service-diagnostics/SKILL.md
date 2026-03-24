---
name: "Systemd Service Diagnostics"
description: "Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.9
reviews: 69
creator: "Tom Anderson"
creator_handle: "@tanderson"
creator_verified: false
source: "https://agentskillexchange.com/skills/systemd-service-diagnostics/"
---
# Systemd Service Diagnostics

Diagnoses systemd service failures using journalctl structured JSON output and systemctl show properties. Analyzes unit file configurations with systemd-analyze verify and detects dependency ordering issues via systemd-analyze dot.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a cursor
```

### OpenClaw

```bash
clawhub install systemd-service-diagnostics
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill systemd-service-diagnostics -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.9/5 (69 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-diagnostics/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
