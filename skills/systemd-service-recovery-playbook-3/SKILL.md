---
name: "Systemd Service Recovery Playbook"
description: "Diagnoses failed systemd units using journalctl structured logging, systemctl show properties, and D-Bus org.freedesktop.systemd1 introspection. Implements graduated recovery with ExecStartPre health checks and watchdog timeout tuning via sd_notify."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "✅ Verified"
rating: "4.8"
reviews: "27"
creator: "Grace Okafor"
creator_handle: "@graceokafor"
creator_verified: "true"
source: "https://agentskillexchange.com/skill/systemd-service-recovery-playbook-3/"
---

# Systemd Service Recovery Playbook

Diagnoses failed systemd units using journalctl structured logging, systemctl show properties, and D-Bus org.freedesktop.systemd1 introspection. Implements graduated recovery with ExecStartPre health checks and watchdog timeout tuning via sd_notify.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install systemd-service-recovery-playbook-3
```

### Claude Code
```bash
claude mcp add systemd-service-recovery-playbook-3
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["systemd-service-recovery-playbook-3"]
}
```

### OpenClaw
```bash
clawhub install systemd-service-recovery-playbook-3
```

### Codex
```bash
codex install systemd-service-recovery-playbook-3
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | ✅ Verified 🔒 Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.8/5 (27 reviews) |

## Creator

**Grace Okafor** ✅
Handle: `@graceokafor`
[View Profile on ASE](https://agentskillexchange.com/skill/systemd-service-recovery-playbook-3/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/systemd-service-recovery-playbook-3/) · [Browse All Skills](https://agentskillexchange.com/skills/)