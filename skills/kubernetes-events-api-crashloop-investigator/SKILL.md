---
title: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
slug: "kubernetes-events-api-crashloop-investigator"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
listed: true
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-events-api-crashloop-investigator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Kubernetes Events API CrashLoop Investigator is designed for operational debugging when a deployment or job keeps restarting and nobody wants to assemble the evidence from scratch every time. It works with the Kubernetes Events API, Pod status and container state fields, and cluster metrics from the Metrics API to show what happened, when it started, and which signals matter most. That makes it well suited for CrashLoopBackOff, ImagePullBackOff, failed readiness checks, and other noisy pod failure modes.
The skill can correlate event timelines with restart counts, last termination reasons, node placement, and recent resource pressure. In practice, that gives responders a more reliable first-pass explanation than reading a single event stream in isolation. It also helps agents produce summaries that point toward configuration, dependency, or resource causes instead of generic statements like “pod is unhealthy.”
Use this skill when you want cluster diagnostics that stay grounded in native Kubernetes APIs and when on-call engineers need a faster, cleaner view of repeated pod startup failures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
