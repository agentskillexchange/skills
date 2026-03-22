---
name: "Systemd Service Recovery Playbook"
description: "Automates systemd service failure diagnosis and recovery using journalctl log analysis and systemctl status inspection. Applies structured runbook logic for common failure modes like socket activat..."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: "verified_metadata"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/systemd-service-recovery-playbook/"
---

# Systemd Service Recovery Playbook

Automates systemd service failure diagnosis and recovery using journalctl log analysis and systemctl status inspection. Applies structured runbook logic for common failure modes like socket activation failures and dependency cycles.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/skills install systemd-service-recovery-playbook
```

### Claude Code
```bash
claude mcp add systemd-service-recovery-playbook
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "systemd-service-recovery-playbook": {
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install systemd-service-recovery-playbook
```

### Codex
```bash
codex install systemd-service-recovery-playbook
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Codex |
| **Verification** | verified_metadata |
| **Rating** | 0 (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/systemd-service-recovery-playbook/)
- [Browse All Skills](https://agentskillexchange.com/)
