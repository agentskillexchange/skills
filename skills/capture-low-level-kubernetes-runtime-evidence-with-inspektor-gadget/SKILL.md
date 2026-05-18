---
name: "Capture low-level Kubernetes runtime evidence with Inspektor Gadget"
slug: "capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget"
description: "Run named Inspektor Gadget traces and snapshots when an agent needs eBPF-backed runtime evidence from pods, containers, or nodes that ordinary logs and metrics do not expose."
github_stars: 2792
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- docker run -ti --rm --privileged -v /:/host --pid=host ghcr.io/inspektor-gadget/ig:latest run trace_open:latest

Requirements and caveats from upstream:
- ### Kubectl Node Debug
- We can use [kubectl node debug](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/) to run ig on a Kubernetes node:
- kubectl debug --profile=sysadmin node/minikube-docker -ti --image=ghcr.io/inspektor-gadget/ig:latest -- ig run trace_open:latest

Basic usage or getting-started notes:
- Security mechanisms to restrict and lock-down which Gadgets can be run
- The following examples use the [trace_open](https://www.inspektor-gadget.io/docs/latest/gadgets/trace_open) Gadget which triggers when a file is open on the system.
- ### Kubernetes

- Source: https://github.com/inspektor-gadget/inspektor-gadget
- Extracted from upstream docs: https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/HEAD/README.md

## Documentation

- https://inspektor-gadget.io/docs/latest/reference/run/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-low-level-kubernetes-runtime-evidence-with-inspektor-gadget/)
