---
title: "Container Runtime Security Monitor"
description: "Monitors container runtime behavior using Falco rules and the Docker Engine API. Detects anomalous syscalls, privilege escalations, and unexpected network connections in real time."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/container-runtime-security-monitor/"
category:
  - "Security &amp; Verification"
framework:
  - "Gemini"
---

# Container Runtime Security Monitor

Runtime security monitoring agent for containerized workloads. Deploys and manages Falco rules to detect suspicious system call patterns including unexpected shell executions, file access in sensitive directories, and privilege escalation attempts. Connects to the Docker Engine API and containerd runtime to monitor container lifecycle events, resource consumption anomalies, and configuration drift. Implements network policy enforcement verification by correlating observed connections against Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom rule authoring with a YAML-based DSL for organization-specific threat models. Streams alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie for incident response.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/container-runtime-security-monitor/)
