---
name: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 4.3
reviews: 48
creator: Raj Gupta
creator_handle: rajgupta
creator_verified: true
source: https://agentskillexchange.com/skill/kubernetes-crashloopbackoff-resolver/
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-crashloopbackoff-resolver
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | 4.3/5 (48 reviews) |

## Creator

**Raj Gupta** (Verified Creator ✓)
- Profile: [@rajgupta](https://agentskillexchange.com/browse-skills/?creator=rajgupta)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-crashloopbackoff-resolver/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
