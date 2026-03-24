---
name: "Systemd Service Recovery Playbook"
description: "Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/"
---

# Systemd Service Recovery Playbook

Diagnoses and recovers failed systemd services using journalctl, systemctl status, and D-Bus org.freedesktop.systemd1 interface. Analyzes exit codes, dependency chains via list-dependencies, and resource limits from cgroup controllers.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a cursor
```

### OpenClaw
```bash
clawhub install systemd-service-recovery-playbook-2
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill systemd-service-recovery-playbook-2 -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/systemd-service-recovery-playbook-2/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
