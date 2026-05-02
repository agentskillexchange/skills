---
title: "Container Runtime Security Monitor"
description: "Monitors container runtime behavior using Falco rules and the Docker Engine API. Detects anomalous syscalls, privilege escalations, and unexpected network connections in real time."
verification: "security_reviewed"
source: "https://github.com/falcosecurity/falco"
category:
  - "Security & Verification"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "falcosecurity/falco"
  github_stars: 8914
---

# Container Runtime Security Monitor

Runtime security monitoring agent for containerized workloads. Deploys and manages Falco rules to detect suspicious system call patterns including unexpected shell executions, file access in sensitive directories, and privilege escalation attempts. Connects to the Docker Engine API and containerd runtime to monitor container lifecycle events, resource consumption anomalies, and configuration drift. Implements network policy enforcement verification by correlating observed connections against Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom rule authoring with a YAML-based DSL for organization-specific threat models. Streams alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie for incident response.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/container-runtime-security-monitor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/container-runtime-security-monitor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/container-runtime-security-monitor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/container-runtime-security-monitor/)
