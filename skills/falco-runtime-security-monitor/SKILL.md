---
title: "Falco Runtime Security Monitor"
description: "Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection."
verification: "security_reviewed"
source: "https://github.com/falcosecurity/falco"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
  - "OpenClaw"
tool_ecosystem:
  github_repo: "falcosecurity/falco"
  github_stars: 8883
---

# Falco Runtime Security Monitor

The Falco Runtime Security Monitor skill provides comprehensive container security monitoring by leveraging the Falco open-source runtime security engine. It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior in containerized workloads. The skill configures Falco rules for detecting shell spawns in containers, unexpected network connections, privilege escalations, and filesystem tampering. It integrates with Kubernetes audit logs to correlate API server events with runtime behavior. Alerts are routed through Prometheus AlertManager with configurable severity levels and notification channels including Slack, PagerDuty, and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams to define organization-specific security policies. Includes automated response capabilities such as pod termination for critical violations and network policy enforcement via Calico or Cilium CNI plugins.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/falco-runtime-security-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/falco-runtime-security-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/falco-runtime-security-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security-monitor/)
