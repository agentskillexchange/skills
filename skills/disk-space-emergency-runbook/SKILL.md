---
name: "Disk Space Emergency Runbook"
description: "Use this skill to quickly identify and clean large files consuming disk space when systems are running critically low. It walks through du, df, lsof, and log rotation commands to free space fast. Trigger when disk usage hits critical thresholds, services are failing due to no space left on device, or disk I/O is saturated."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed
rating: 4.7
reviews: 76
creator: Kai Nakamura
creator_handle: kainakamura
creator_verified: true
source: https://agentskillexchange.com/skill/disk-space-emergency-runbook/
---

# Disk Space Emergency Runbook

Use this skill to quickly identify and clean large files consuming disk space when systems are running critically low. It walks through du, df, lsof, and log rotation commands to free space fast. Trigger when disk usage hits critical thresholds, services are failing due to no space left on device, or disk I/O is saturated.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a cursor
```

### OpenClaw

```bash
clawhub install disk-space-emergency-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill disk-space-emergency-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Monitoring & Alerts |
| Framework | Custom Agents |
| Verification | Security Reviewed |
| Rating | 4.7/5 (76 reviews) |

## Creator

**Kai Nakamura** (Verified Creator ✓)
- Profile: [@kainakamura](https://agentskillexchange.com/browse-skills/?creator=kainakamura)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/disk-space-emergency-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
