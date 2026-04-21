---
title: "Kubernetes Runbook Executor"
slug: "kubernetes-runbook-executor-2"
description: "Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/)
