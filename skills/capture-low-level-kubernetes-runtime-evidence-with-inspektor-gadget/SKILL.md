---
title: "Capture low-level Kubernetes runtime evidence with Inspektor Gadget"
description: "Run named Inspektor Gadget traces and snapshots when an agent needs eBPF-backed runtime evidence from pods, containers, or nodes that ordinary logs and metrics do not expose."
verification: "listed"
source: "https://github.com/inspektor-gadget/inspektor-gadget"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "inspektor-gadget/inspektor-gadget"
  github_stars: 2792
---

# Capture low-level Kubernetes runtime evidence with Inspektor Gadget

Use Inspektor Gadget when an agent needs kernel-level or container-runtime evidence to explain behavior that higher-level telemetry missed. It runs named gadgets such as trace_exec, trace_tcp, and snapshot_process to collect targeted eBPF-backed data from Kubernetes workloads and Linux hosts. Invoke it during deep incident response, runtime debugging, and low-level troubleshooting after the usual logs, events, and dashboards stop being enough. The scope boundary is clear: this skill is about selecting and running purpose-built gadgets to capture specific runtime evidence, not about serving as a generic Kubernetes management or observability product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget/)
