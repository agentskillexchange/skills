---
title: "Kubernetes CrashLoop Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
slug: "kubernetes-crashloop-diagnoser-agent"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/"
---

# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-crashloop-diagnoser-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes.
The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches.
Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
