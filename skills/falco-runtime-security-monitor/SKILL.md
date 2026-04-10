---
name: Falco Runtime Security Monitor
description: Monitors container runtime events using Falco sysdig libraries and sends
  alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and
  Prometheus AlertManager for real-time threat detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/falco-runtime-security-monitor/
category:
- Security &amp; Verification
framework:
- Multi-Framework
- OpenClaw
---
# Falco Runtime Security Monitor

The Falco Runtime Security Monitor skill provides comprehensive container security monitoring by leveraging the Falco open-source runtime security engine. It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior in containerized workloads. The skill configures Falco rules for detecting shell spawns in containers, unexpected network connections, privilege escalations, and filesystem tampering. It integrates with Kubernetes audit logs to correlate API server events with runtime behavior. Alerts are routed through Prometheus AlertManager with configurable severity levels and notification channels including Slack, PagerDuty, and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams to define organization-specific security policies. Includes automated response capabilities such as pod termination for critical violations and network policy enforcement via Calico or Cilium CNI plugins.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security-monitor/)
