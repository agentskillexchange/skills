---
name: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---
# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Overview

Kubernetes Events API CrashLoop Investigator is designed for operational debugging when a deployment or job keeps restarting and nobody wants to assemble the evidence from scratch every time. It works with the Kubernetes Events API, Pod status and container state fields, and cluster metrics from the Metrics API to show what happened, when it started, and which signals matter most. That makes it well suited for CrashLoopBackOff, ImagePullBackOff, failed readiness checks, and other noisy pod failure modes.

The skill can correlate event timelines with restart counts, last termination reasons, node placement, and recent resource pressure. In practice, that gives responders a more reliable first-pass explanation than reading a single event stream in isolation. It also helps agents produce summaries that point toward configuration, dependency, or resource causes instead of generic statements like “pod is unhealthy.”

Use this skill when you want cluster diagnostics that stay grounded in native Kubernetes APIs and when on-call engineers need a faster, cleaner view of repeated pod startup failures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-events-api-crashloop-investigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-events-api-crashloop-investigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-events-api-crashloop-investigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-events-api-crashloop-investigator -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-events-api-crashloop-investigator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
