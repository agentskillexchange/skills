---
title: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes CrashLoopBackOff Resolver

The Kubernetes CrashLoopBackOff Resolver automates diagnosis of pods stuck in CrashLoopBackOff state using the Kubernetes API server. It queries the /api/v1/namespaces/{ns}/pods endpoint to identify failing pods, then retrieves container status details including exit codes, restart counts, and last termination reasons.


The agent uses kubectl logs –previous to capture logs from the last crashed container instance, parsing for common failure patterns including uncaught exceptions, missing environment variables, and failed health check responses. It integrates with the container runtime via crictl inspect to examine container-level resource limits, security contexts, and volume mount configurations.


For OOMKilled events, it queries the Kubernetes Metrics API via metrics-server to analyze memory usage trends leading up to the kill. It checks ConfigMap and Secret references via the Kubernetes API, validates image availability using the Docker Registry HTTP API v2 /manifests endpoint, and verifies node resource pressure conditions through the Node Status API. Remediation suggestions include resource limit adjustments, probe timing recommendations, and init container dependency fixes.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/)
