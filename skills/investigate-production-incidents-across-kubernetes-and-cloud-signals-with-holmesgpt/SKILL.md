---
title: "Investigate production incidents across Kubernetes and cloud signals with HolmesGPT"
description: "Use HolmesGPT when an on-call agent needs one investigation loop that pulls alerts, logs, metrics, and infrastructure context from multiple systems and returns a root-cause path instead of forcing a human to hop across separate observability products."
verification: "security_reviewed"
source: "https://github.com/HolmesGPT/holmesgpt"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "HolmesGPT/holmesgpt"
  github_stars: 2265
---

# Investigate production incidents across Kubernetes and cloud signals with HolmesGPT

HolmesGPT is publishable because the user-facing job is specific and operational: investigate a live production incident by querying connected observability and infrastructure systems, correlate the evidence, and return a likely root-cause path with remediation direction. The upstream project explicitly frames itself as an open-source AI agent for production incident investigation, with built-in integrations for Kubernetes, Prometheus, Grafana, Datadog, cloud services, databases, ticketing systems, and more. Invoke it instead of using the underlying products normally when the real need is cross-source incident investigation, not dashboard-by-dashboard inspection. A user reaches for HolmesGPT when an agent should gather the relevant signals, follow the evidence across systems, and explain what is probably broken, rather than manually pivot through kubectl, alerting tools, logs, traces, and cloud consoles. The scope boundary is clear enough to keep this from collapsing into a plain product card: this is not a generic observability platform listing and not just a connector bundle. The bounded workflow is incident triage and root-cause investigation across existing telemetry sources. That is a concrete agent job to be done with a tighter operator outcome than the surrounding platforms HolmesGPT connects to.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt/)
