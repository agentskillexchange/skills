---
name: "Falco Runtime Security Monitor"
description: "Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection."
category: "Security & Verification"
framework: "Multi-Framework"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/falco-runtime-security-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Falco Runtime Security Monitor

Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection.

## Overview

The Falco Runtime Security Monitor skill provides comprehensive container security monitoring by leveraging the Falco open-source runtime security engine. It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior in containerized workloads. The skill configures Falco rules for detecting shell spawns in containers, unexpected network connections, privilege escalations, and filesystem tampering. It integrates with Kubernetes audit logs to correlate API server events with runtime behavior. Alerts are routed through Prometheus AlertManager with configurable severity levels and notification channels including Slack, PagerDuty, and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams to define organization-specific security policies. Includes automated response capabilities such as pod termination for critical violations and network policy enforcement via Calico or Cilium CNI plugins.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security-monitor -a codex
```

### OpenClaw

```bash
clawhub install falco-runtime-security-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/falco-runtime-security-monitor/
