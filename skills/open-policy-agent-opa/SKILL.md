---
name: "Open Policy Agent (OPA)"
description: "Open Policy Agent (OPA) is built around Kubernetes orchestration platform. The underlying ecosystem is represented by kubernetes/kubernetes (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving […]"
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/open-policy-agent-opa/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121334  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Open Policy Agent (OPA)

Open Policy Agent (OPA) is built around Kubernetes orchestration platform. The underlying ecosystem is represented by kubernetes/kubernetes (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving […]

## Overview

**Open Policy Agent (OPA)** is built around Kubernetes orchestration platform. The underlying ecosystem is represented by `kubernetes/kubernetes` (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to kubernetes so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on kubectl, API server, pods, deployments, events, logs, probes, RBAC, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses kubectl, API server, pods, deployments, events, logs, probes, RBAC instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as cluster operations, workload health, scaling, and production troubleshooting.

In security-oriented usage, the skill emphasizes read-only discovery, evidence capture, and machine-readable output such as SARIF, JSON, or structured findings so results can flow into existing review pipelines. Key integration points include cluster operations, workload health, scaling, and production troubleshooting. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill open-policy-agent-opa
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill open-policy-agent-opa -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill open-policy-agent-opa -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill open-policy-agent-opa -a codex
```

### OpenClaw

```bash
clawhub install open-policy-agent-opa
```

## Source

- Marketplace: https://agentskillexchange.com/skills/open-policy-agent-opa/
