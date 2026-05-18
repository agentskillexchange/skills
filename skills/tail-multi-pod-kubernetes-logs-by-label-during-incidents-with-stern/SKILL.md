---
name: "Tail multi-pod Kubernetes logs by label during incidents with Stern"
slug: "tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern"
description: "Aggregate and follow logs from matching Kubernetes pods during incident triage without hopping pod by pod."
github_stars: 4636
verification: "listed"
source: "https://github.com/stern/stern"
author: "Stern maintainers"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "stern/stern"
  github_stars: 4636
---

# Tail multi-pod Kubernetes logs by label during incidents with Stern

Aggregate and follow logs from matching Kubernetes pods during incident triage without hopping pod by pod.

## Prerequisites

Stern CLI, Kubernetes cluster access

## Installation

Use the upstream install or setup path that matches your environment:
- go install github.com/stern/stern@latest
- brew install stern
- brew install bash-completion
- brew install bash-completion@2

Requirements and caveats from upstream:
- --container-colors | | Specifies the colors used to highlight container names. Use the same format as --pod-colors. Defaults to the values of --pod-colors if omitted, and must match its length.
- --node | | Node name to filter on.
- | NodeName | string | The node name where the pod is scheduled on |

Basic usage or getting-started notes:
- ### Download binary
- Download a [binary release](https://github.com/stern/stern/releases)
- ### Build from source

- Source: https://github.com/stern/stern
- Extracted from upstream docs: https://raw.githubusercontent.com/stern/stern/HEAD/README.md

## Documentation

- https://github.com/stern/stern

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)
