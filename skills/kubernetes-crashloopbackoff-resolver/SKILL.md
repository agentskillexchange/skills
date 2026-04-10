---
name: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs -previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
---

# Kubernetes CrashLoopBackOff Resolver

The Kubernetes CrashLoopBackOff Resolver automates diagnosis of pods stuck in CrashLoopBackOff state using the Kubernetes API server. It queries the /api/v1/namespaces/{ns}/pods endpoint to identify failing pods, then retrieves container status details including exit codes, restart counts, and last termination reasons.
The agent uses kubectl logs -previous to capture logs from the last crashed container instance, parsing for common failure patterns including uncaught exceptions, missing environment variables, and failed health check responses. It integrates with the container runtime via crictl inspect to examine container-level resource limits, security contexts, and volume mount configurations.
For OOMKilled events, it queries the Kubernetes Metrics API via metrics-server to analyze memory usage trends leading up to the kill. It checks ConfigMap and Secret references via the Kubernetes API, validates image availability using the Docker Registry HTTP API v2 /manifests endpoint, and verifies node resource pressure conditions through the Node Status API. Remediation suggestions include resource limit adjustments, probe timing recommendations, and init container dependency fixes.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
