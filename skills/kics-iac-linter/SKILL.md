---
name: "KICS IaC Linter"
description: "Checkmarx KICS (Keeping Infrastructure as Code Secure) scans Terraform, CloudFormation, Ansible, Kubernetes, and Dockerfile for security vulnerabilities, compliance issues, and best practice violations."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kics-iac-linter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# KICS IaC Linter

Checkmarx KICS (Keeping Infrastructure as Code Secure) scans Terraform, CloudFormation, Ansible, Kubernetes, and Dockerfile for security vulnerabilities, compliance issues, and best practice violations.

## Overview

Checkmarx KICS (Keeping Infrastructure as Code Secure) scans Terraform, CloudFormation, Ansible, Kubernetes, and Dockerfile for security vulnerabilities, compliance issues, and best practice violations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kics-iac-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kics-iac-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kics-iac-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kics-iac-linter -a codex
```

### OpenClaw

```bash
clawhub install kics-iac-linter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kics-iac-linter/
