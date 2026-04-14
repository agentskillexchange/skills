---
title: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoopBackOff Resolver

The Kubernetes CrashLoopBackOff Resolver automates diagnosis of pods stuck in CrashLoopBackOff state using the Kubernetes API server. It queries the /api/v1/namespaces/{ns}/pods endpoint to identify failing pods, then retrieves container status details including exit codes, restart counts, and last termination reasons.

The agent uses kubectl logs –previous to capture logs from the last crashed container instance, parsing for common failure patterns including uncaught exceptions, missing environment variables, and failed health check responses. It integrates with the container runtime via crictl inspect to examine container-level resource limits, security contexts, and volume mount configurations.

For OOMKilled events, it queries the Kubernetes Metrics API via metrics-server to analyze memory usage trends leading up to the kill. It checks ConfigMap and Secret references via the Kubernetes API, validates image availability using the Docker Registry HTTP API v2 /manifests endpoint, and verifies node resource pressure conditions through the Node Status API. Remediation suggestions include resource limit adjustments, probe timing recommendations, and init container dependency fixes.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
