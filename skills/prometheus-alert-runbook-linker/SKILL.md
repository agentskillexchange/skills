---
name: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.0
reviews: 82
creator: Sofia Petrov
creator_handle: sofiapetrov
creator_verified: true
source: https://agentskillexchange.com/skill/prometheus-alert-runbook-linker/
---

# Prometheus Alert Runbook Linker

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a cursor
```

### OpenClaw

```bash
clawhub install prometheus-alert-runbook-linker
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | 4.0/5 (82 reviews) |

## Creator

**Sofia Petrov** (Verified Creator ✓)
- Profile: [@sofiapetrov](https://agentskillexchange.com/browse-skills/?creator=sofiapetrov)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/prometheus-alert-runbook-linker/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
