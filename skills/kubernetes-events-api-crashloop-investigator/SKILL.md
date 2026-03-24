---
name: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
category: "Runbooks &amp; Diagnostics"
framework: ""
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/"
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills add kubernetes-events-api-crashloop-investigator
```

### Claude Code
```bash
npx @anthropic/agent-skills add kubernetes-events-api-crashloop-investigator --target claude-code
```

### Cursor
```bash
npx @anthropic/agent-skills add kubernetes-events-api-crashloop-investigator --target cursor
```

### Codex
```bash
npx @anthropic/agent-skills add kubernetes-events-api-crashloop-investigator --target codex
```

### OpenClaw
```bash
clawhub install kubernetes-events-api-crashloop-investigator
```
