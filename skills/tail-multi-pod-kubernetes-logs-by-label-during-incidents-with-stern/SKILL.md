---
title: "Tail multi-pod Kubernetes logs by label during incidents with Stern"
slug: "tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern"
description: "Aggregate and follow logs from matching Kubernetes pods during incident triage without hopping pod by pod."
github_stars: 4636
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Stern from the project repository or package manager, then run it against a namespace, label selector, or pod name pattern to stream matching logs during investigation.
```

## Documentation

- https://github.com/stern/stern

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern/)
