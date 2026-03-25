---
name: "Open Policy Agent (OPA)"
description: "Implements policy-as-code using Open Policy Agent and Rego language. Enforces admission control in Kubernetes, API authorization policies, and infrastructure compliance checks across cloud resources."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/open-policy-agent-opa/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Open Policy Agent (OPA)

Implements policy-as-code using Open Policy Agent and Rego language. Enforces admission control in Kubernetes, API authorization policies, and infrastructure compliance checks across cloud resources.

## Overview

Implements policy-as-code using Open Policy Agent and Rego language. Enforces admission control in Kubernetes, API authorization policies, and infrastructure compliance checks across cloud resources.

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
