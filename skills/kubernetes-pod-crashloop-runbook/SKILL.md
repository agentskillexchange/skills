---
title: "Kubernetes Pod Crashloop Runbook"
description: "Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crashloop Runbook

This skill queries the Kubernetes API server (typically at /api/v1 and /apis/apps/v1) using a kubeconfig or in-cluster service account token. When a pod enters CrashLoopBackOff, the skill fetches the last 100 lines of container logs via the pods/log subresource, retrieves pod events from the Events API, and checks resource quota limits in the namespace. It distinguishes between OOMKilled (memory limit exceeded), probe failures (liveness/readiness misconfiguration), and missing dependencies (ConfigMap or Secret not found). The skill cross-references the pod spec against the namespace ResourceQuota and LimitRange objects. A step-by-step Markdown runbook is generated with specific kubectl commands to apply, including suggested resource limit adjustments and probe timeout fixes. Compatible with Kubernetes 1.25+.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
