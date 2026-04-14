---
title: "Kubernetes Incident Runbook"
description: "Executes structured incident response procedures for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Events API. Automates pod crash diagnosis, OOMKill analysis, and node pressure triage."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Incident Runbook

The Kubernetes Incident Runbook skill provides automated incident response procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes API, and kube-state-metrics to systematically diagnose common failure modes including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions.

When triggered, the skill follows a structured diagnostic tree. For pod failures, it inspects container exit codes, retrieves previous container logs via kubectl logs –previous, checks resource requests/limits against actual usage from metrics-server, and examines events for scheduling or volume mount failures.

For node-level issues, it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks kubelet logs, inspects systemd service status, and correlates with cloud provider instance health. The skill understands taints, tolerations, and affinity rules that may cause scheduling failures.

Advanced capabilities include tracing network connectivity issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim binding failures across storage classes, and identifying resource quota exhaustion across namespaces. All findings are compiled into structured incident reports with remediation steps.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-incident-runbook/)
