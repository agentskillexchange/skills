---
title: "Probe Kubernetes clusters for exposed attack paths with kube-hunter"
description: "Assess a Kubernetes cluster from the attacker viewpoint when an agent needs exposure-focused findings instead of a general cluster scanner listing."
verification: "listed"
source: "https://github.com/aquasecurity/kube-hunter"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aquasecurity/kube-hunter"
  github_stars: 5040
---

# Probe Kubernetes clusters for exposed attack paths with kube-hunter

Use kube-hunter when an agent needs to probe a Kubernetes environment from an attacker’s perspective and surface reachable weaknesses such as exposed dashboards, insecure ports, or risky cluster configurations. It is appropriate for offensive validation, external exposure review, and security triage where the workflow is to run the probe, inspect findings, and hand back attack-path evidence. The scope boundary is specific: this skill is about exposure-oriented cluster probing, not full cluster administration or a generic Kubernetes security platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/probe-kubernetes-clusters-for-exposed-attack-paths-with-kube-hunter/)
