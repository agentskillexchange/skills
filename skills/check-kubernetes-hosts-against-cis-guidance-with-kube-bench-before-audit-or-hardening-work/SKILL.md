---
title: "Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work"
description: "Run a benchmark-driven posture check on Kubernetes nodes and control planes before an audit, upgrade, or hardening sprint starts."
verification: "listed"
source: "https://github.com/aquasecurity/kube-bench"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-bench"
  github_stars: 7788
---

# Check Kubernetes hosts against CIS guidance with kube-bench before audit or hardening work

Use kube-bench when an agent needs a benchmark-oriented security posture check against CIS guidance, not when a user is just operating Kubernetes normally. The workflow is narrow: inspect host and cluster configuration, map findings to CIS controls, and hand back concrete remediation items. That scope boundary, standards-based posture verification for Kubernetes environments, keeps it distinct from a broad Kubernetes platform or generic scanner listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-kubernetes-hosts-against-cis-guidance-with-kube-bench-before-audit-or-hardening-work/)
