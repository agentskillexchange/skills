---
name: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: verified_metadata
rating: 4.5
reviews: 49
creator: "Elena Kowalski"
creator_handle: "@ekowalski"
creator_verified: true
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
---
# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a cursor
```

### OpenClaw

```bash
clawhub install pulumi-drift-detector-reconciler
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Verified Metadata |
| Rating | 4.5/5 (49 reviews) |

## Creator

**Elena Kowalski** (Verified Creator ✓)
- Profile: [@ekowalski](https://agentskillexchange.com/browse-skills/?creator=ekowalski)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
