---
title: "Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work"
slug: "check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work"
description: "Run a benchmark-driven posture check on Kubernetes nodes and control planes before an audit, upgrade, or hardening sprint starts."
github_stars: 7788
verification: "security_reviewed"
source: "https://github.com/aquasecurity/kube-bench"
author: "Aqua Security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-bench"
  github_stars: 7788
---

# Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work

Run a benchmark-driven posture check on Kubernetes nodes and control planes before an audit, upgrade, or hardening sprint starts.

## Prerequisites

kube-bench binary or container image, access to Kubernetes nodes or cluster context, benchmark profile matching the target environment

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install kube-bench from the upstream release or container image, run it with the documented permissions against the target nodes or cluster, then review the generated CIS control findings and remediation guidance.
```

## Documentation

- https://github.com/aquasecurity/kube-bench

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work/)
