---
name: "Falco Runtime Security"
description: "Deploys and manages Falco rules for kernel-level runtime security monitoring in Kubernetes. Detects anomalous behavior, privilege escalations, unexpected network connections, and file system access violations."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/falco-runtime-security/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Falco Runtime Security

Deploys and manages Falco rules for kernel-level runtime security monitoring in Kubernetes. Detects anomalous behavior, privilege escalations, unexpected network connections, and file system access violations.

## Overview

Deploys and manages Falco rules for kernel-level runtime security monitoring in Kubernetes. Detects anomalous behavior, privilege escalations, unexpected network connections, and file system access violations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill falco-runtime-security -a codex
```

### OpenClaw

```bash
clawhub install falco-runtime-security
```

## Source

- Marketplace: https://agentskillexchange.com/skills/falco-runtime-security/
