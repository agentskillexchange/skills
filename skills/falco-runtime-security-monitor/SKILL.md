---
title: "Falco Runtime Security Monitor"
description: "Monitors container runtime events using Falco sysdig libraries and sends alerts on suspicious syscall patterns. Integrates with Kubernetes audit logs and Prometheus AlertManager for real-time threat detection."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/falco-runtime-security-monitor/"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
  - "OpenClaw"
---

# Falco Runtime Security Monitor

The Falco Runtime Security Monitor skill provides comprehensive container security monitoring by leveraging the Falco open-source runtime security engine. It hooks into Linux kernel syscalls via eBPF probes to detect anomalous behavior in containerized workloads. The skill configures Falco rules for detecting shell spawns in containers, unexpected network connections, privilege escalations, and filesystem tampering. It integrates with Kubernetes audit logs to correlate API server events with runtime behavior. Alerts are routed through Prometheus AlertManager with configurable severity levels and notification channels including Slack, PagerDuty, and OpsGenie. The skill also supports custom Falco rule authoring, allowing teams to define organization-specific security policies. Includes automated response capabilities such as pod termination for critical violations and network policy enforcement via Calico or Cilium CNI plugins.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security-monitor/)
