---
title: "Kubernetes CrashLoop Diagnostician"
slug: "kubernetes-crashloop-diagnostician"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnostician

Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/)
