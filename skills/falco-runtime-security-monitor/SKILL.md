---
name: "Falco Runtime Security Monitor"
description: "Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection."
category: "Security &amp; Verification"
framework: "Multi-Framework, OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/falco-runtime-security-monitor/"
---
# Falco Runtime Security Monitor

Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection.

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

## Details

The Falco Runtime Security Monitor skill provides comprehensive container security monitoring by leveraging the Falco open-source runtime security engine. It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior in containerized workloads. The skill configures Falco rules for detecting shell spawns in containers, unexpected network connections, privilege escalations, and filesystem tampering. It integrates with Kubernetes audit logs to correlate API server events with runtime behavior. Alerts are routed through Prometheus AlertManager with configurable severity levels and notification channels including Slack, PagerDuty, and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams to define organization-specific security policies. Includes automated response capabilities such as pod termination for critical violations and network policy enforcement via Calico or Cilium CNI plugins.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security-monitor/)
