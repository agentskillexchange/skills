---
name: "Terrascan Policy Scanner"
description: "Tenable Terrascan scans Terraform, Kubernetes, Helm, and CloudFormation for security vulnerabilities and compliance violations. Maps findings to NIST, CIS, and GDPR controls with fix guidance."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terrascan-policy-scanner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terrascan Policy Scanner

Tenable Terrascan scans Terraform, Kubernetes, Helm, and CloudFormation for security vulnerabilities and compliance violations. Maps findings to NIST, CIS, and GDPR controls with fix guidance.

## Overview

Tenable Terrascan scans Terraform, Kubernetes, Helm, and CloudFormation for security vulnerabilities and compliance violations. Maps findings to NIST, CIS, and GDPR controls with fix guidance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terrascan-policy-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terrascan-policy-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terrascan-policy-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terrascan-policy-scanner -a codex
```

### OpenClaw

```bash
clawhub install terrascan-policy-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terrascan-policy-scanner/
