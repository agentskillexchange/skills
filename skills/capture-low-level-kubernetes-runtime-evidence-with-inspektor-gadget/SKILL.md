---
name: "Capture low-level Kubernetes runtime evidence with Inspektor Gadget"
slug: "capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget"
description: "Run named Inspektor Gadget traces and snapshots when an agent needs eBPF-backed runtime evidence from pods, containers, or nodes that ordinary logs and metrics do not expose."
github_stars: 2792
verification: "security_reviewed"
source: "https://github.com/inspektor-gadget/inspektor-gadget"
author: "Inspektor Gadget"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "inspektor-gadget/inspektor-gadget"
  github_stars: 2792
---

# Capture low-level Kubernetes runtime evidence with Inspektor Gadget

Run named Inspektor Gadget traces and snapshots when an agent needs eBPF-backed runtime evidence from pods, containers, or nodes that ordinary logs and metrics do not expose.

## Prerequisites

Inspektor Gadget installed on Kubernetes or Linux with permissions to run gadgets

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kubectl-gadget via krew or install the ig binary, then run a named gadget such as kubectl gadget run trace_exec:latest or ig run trace_open:latest against the target environment.
```

## Documentation

- https://inspektor-gadget.io/docs/latest/reference/run/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget/)
