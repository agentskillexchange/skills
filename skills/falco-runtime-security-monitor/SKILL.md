---
title: Falco Runtime Security Monitor
description: The Falco Runtime Security Monitor skill provides comprehensive container
  security monitoring by leveraging the Falco open-source runtime security engine.
  It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior
  in containerized workloads. The skill configures Falco rules for detecting shell
  spawns in containers, unexpected network connections, privilege escalations, and
  filesystem tampering. It integrates with Kubernetes audit logs to correlate API
  server events with runtime behavior. Alerts are routed through Prometheus AlertManager
  with configurable severity levels and notification channels including Slack, PagerDuty,
  and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams
  to define organization-specific security policies. Includes automated response capabilities
  such as pod termination for critical violations and network policy enforcement via
  Calico or Cilium CNI plugins.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security-monitor/)
