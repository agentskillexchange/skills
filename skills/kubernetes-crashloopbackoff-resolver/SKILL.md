---
name: "Kubernetes CrashLoopBackOff Resolver"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs –previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Overview

The Kubernetes CrashLoopBackOff Resolver automates diagnosis of pods stuck in CrashLoopBackOff state using the Kubernetes API server. It queries the /api/v1/namespaces/{ns}/pods endpoint to identify failing pods, then retrieves container status details including exit codes, restart counts, and last termination reasons.

The agent uses kubectl logs –previous to capture logs from the last crashed container instance, parsing for common failure patterns including uncaught exceptions, missing environment variables, and failed health check responses. It integrates with the container runtime via crictl inspect to examine container-level resource limits, security contexts, and volume mount configurations.

For OOMKilled events, it queries the Kubernetes Metrics API via metrics-server to analyze memory usage trends leading up to the kill. It checks ConfigMap and Secret references via the Kubernetes API, validates image availability using the Docker Registry HTTP API v2 /manifests endpoint, and verifies node resource pressure conditions through the Node Status API. Remediation suggestions include resource limit adjustments, probe timing recommendations, and init container dependency fixes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-crashloopbackoff-resolver
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-crashloopbackoff-resolver/
