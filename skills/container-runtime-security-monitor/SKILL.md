---
title: Container Runtime Security Monitor
description: Runtime security monitoring agent for containerized workloads. Deploys
  and manages Falco rules to detect suspicious system call patterns including unexpected
  shell executions, file access in sensitive directories, and privilege escalation
  attempts. Connects to the Docker Engine API and containerd runtime to monitor container
  lifecycle events, resource consumption anomalies, and configuration drift. Implements
  network policy enforcement verification by correlating observed connections against
  Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior
  through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom
  rule authoring with a YAML-based DSL for organization-specific threat models. Streams
  alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie
  for incident response.
verification: security_reviewed
source: https://agentskillexchange.com/skills/container-runtime-security-monitor/
category:
- Security &amp; Verification
framework:
- Gemini
---

# Container Runtime Security Monitor

Runtime security monitoring agent for containerized workloads. Deploys and manages Falco rules to detect suspicious system call patterns including unexpected shell executions, file access in sensitive directories, and privilege escalation attempts. Connects to the Docker Engine API and containerd runtime to monitor container lifecycle events, resource consumption anomalies, and configuration drift. Implements network policy enforcement verification by correlating observed connections against Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom rule authoring with a YAML-based DSL for organization-specific threat models. Streams alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie for incident response.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/container-runtime-security-monitor/)
