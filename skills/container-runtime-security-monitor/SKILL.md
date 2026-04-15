---
title: "Container Runtime Security Monitor"
description: "Monitors container runtime behavior using Falco rules and the Docker Engine API. Detects anomalous syscalls, privilege escalations, and unexpected network connections in real time."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/container-runtime-security-monitor/"
category:
  - "Security & Verification"
framework:
  - "Gemini"
---

# Container Runtime Security Monitor

Runtime security monitoring agent for containerized workloads. Deploys and manages Falco rules to detect suspicious system call patterns including unexpected shell executions, file access in sensitive directories, and privilege escalation attempts. Connects to the Docker Engine API and containerd runtime to monitor container lifecycle events, resource consumption anomalies, and configuration drift. Implements network policy enforcement verification by correlating observed connections against Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom rule authoring with a YAML-based DSL for organization-specific threat models. Streams alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie for incident response.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/container-runtime-security-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/container-runtime-security-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/container-runtime-security-monitor/)
