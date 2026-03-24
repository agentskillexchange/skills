---
name: "Checkov IaC Scanner"
description: "Scans Terraform, CloudFormation, Kubernetes manifests, ARM templates, and Dockerfiles for security misconfigurations and compliance violations. Maps findings to CIS benchmarks and SOC2 controls."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/checkov-iac-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Checkov IaC Scanner

Scans Terraform, CloudFormation, Kubernetes manifests, ARM templates, and Dockerfiles for security misconfigurations and compliance violations. Maps findings to CIS benchmarks and SOC2 controls.

## Overview

Scans Terraform, CloudFormation, Kubernetes manifests, ARM templates, and Dockerfiles for security misconfigurations and compliance violations. Maps findings to CIS benchmarks and SOC2 controls.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill checkov-iac-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill checkov-iac-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill checkov-iac-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill checkov-iac-scanner -a codex
```

### OpenClaw

```bash
clawhub install checkov-iac-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/checkov-iac-scanner/
