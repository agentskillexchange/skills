---
name: "Systemd Service Recovery Playbook"
description: "Diagnoses failed systemd units using journalctl structured logging, systemctl show properties, and D-Bus org.freedesktop.systemd1 introspection. Implements graduated recovery with ExecStartPre health checks and watchdog timeout tuning via sd_notify."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.8
reviews: 27
creator: "Grace Okafor"
creator_handle: "@graceokafor"
creator_verified: true
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-3/"
---
# Systemd Service Recovery Playbook

Diagnoses failed systemd units using journalctl structured logging, systemctl show properties, and D-Bus org.freedesktop.systemd1 introspection. Implements graduated recovery with ExecStartPre health checks and watchdog timeout tuning via sd_notify.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-3
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-3 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-3 -a cursor
```

### OpenClaw
```bash
clawhub install systemd-service-recovery-playbook-3
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-3 -a codex
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