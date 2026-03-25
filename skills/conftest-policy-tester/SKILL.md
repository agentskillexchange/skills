---
name: "Conftest Policy Tester"
description: "Tests configuration files (Kubernetes manifests, Terraform, Dockerfiles, Helm charts) against OPA Rego policies using Conftest. Integrates into CI/CD to prevent policy violations from reaching production."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/conftest-policy-tester/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Conftest Policy Tester

Tests configuration files (Kubernetes manifests, Terraform, Dockerfiles, Helm charts) against OPA Rego policies using Conftest. Integrates into CI/CD to prevent policy violations from reaching production.

## Overview

Tests configuration files (Kubernetes manifests, Terraform, Dockerfiles, Helm charts) against OPA Rego policies using Conftest. Integrates into CI/CD to prevent policy violations from reaching production.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill conftest-policy-tester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill conftest-policy-tester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill conftest-policy-tester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill conftest-policy-tester -a codex
```

### OpenClaw

```bash
clawhub install conftest-policy-tester
```

## Source

- Marketplace: https://agentskillexchange.com/skills/conftest-policy-tester/
