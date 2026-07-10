---
title: "Run declarative Kubernetes test suites against clusters before operator or manifest changes merge with KUTTL"
description: "Express Kubernetes test steps and assertions in YAML, then execute them against a real cluster before shipping controller or manifest changes."
verification: "security_reviewed"
source: "https://github.com/kudobuilder/kuttl"
author: "kudobuilder"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kudobuilder/kuttl"
  github_stars: 804
---

# Run declarative Kubernetes test suites against clusters before operator or manifest changes merge with KUTTL

Express Kubernetes test steps and assertions in YAML, then execute them against a real cluster before shipping controller or manifest changes.

## Prerequisites

KUTTL CLI or kubectl-kuttl plugin, access to a Kubernetes test cluster, declarative test step YAML files, and the manifests or operators under test

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install KUTTL from the upstream release or plugin instructions, author the documented test suite structure with steps and assertions, then run the test command against a Kubernetes cluster prepared for the target manifests or operator.
```

## Documentation

- https://github.com/kudobuilder/kuttl

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-declarative-kubernetes-test-suites-against-clusters-before-operator-or-manifest-changes-merge-with-kuttl/)
