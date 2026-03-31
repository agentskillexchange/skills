---
name: "Container Runtime Security Monitor"
description: "Monitors container runtime behavior using Falco rules and the Docker Engine API. Detects anomalous syscalls, privilege escalations, and unexpected network connections in real time."
category: "Security &amp; Verification"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/container-runtime-security-monitor/"
---
# Container Runtime Security Monitor

Monitors container runtime behavior using Falco rules and the Docker Engine API. Detects anomalous syscalls, privilege escalations, and unexpected network connections in real time.

## Overview

Runtime security monitoring agent for containerized workloads. Deploys and manages Falco rules to detect suspicious system call patterns including unexpected shell executions, file access in sensitive directories, and privilege escalation attempts. Connects to the Docker Engine API and containerd runtime to monitor container lifecycle events, resource consumption anomalies, and configuration drift. Implements network policy enforcement verification by correlating observed connections against Kubernetes NetworkPolicy definitions via the K8s API. Detects cryptomining behavior through CPU usage pattern analysis and known mining pool DNS lookups. Supports custom rule authoring with a YAML-based DSL for organization-specific threat models. Streams alerts to SIEM systems via Syslog and webhook integrations with PagerDuty and OpsGenie for incident response.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill container-runtime-security-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill container-runtime-security-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill container-runtime-security-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill container-runtime-security-monitor -a codex
```

### OpenClaw

```bash
clawhub install container-runtime-security-monitor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/container-runtime-security-monitor/)
