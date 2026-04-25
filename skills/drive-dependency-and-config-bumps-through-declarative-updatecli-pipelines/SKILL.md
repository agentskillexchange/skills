---
title: "Drive dependency and config bumps through declarative Updatecli pipelines"
description: "Use Updatecli when an agent needs to detect upstream releases, validate conditions, patch versioned files, and open reviewable update actions from one policy run instead of hand-editing manifests or relying on a single ecosystem bot."
verification: "security_reviewed"
source: "https://github.com/updatecli/updatecli"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "updatecli/updatecli"
  github_stars: 894
---

# Drive dependency and config bumps through declarative Updatecli pipelines

Best for: teams that want an agent to watch upstream versions, patch config files or manifests, and produce reviewable update changes across repositories without hard-coding one package manager workflow. Updatecli is a declarative update policy engine. A policy file defines sources to discover a value, conditions to validate it, and targets to write the change. That makes it a strong fit for agent-driven maintenance runs where the goal is not just “check for updates” but “detect, validate, patch, and hand off a reviewable change set.” When to invoke it Invoke this skill when you want an agent to keep Docker tags, Helm values, GitOps manifests, CI images, or version pins current through one reproducible policy run. It is especially useful when the update spans multiple files or requires gating logic before a change should be written. Scope boundary This is not a general product listing for the Updatecli platform. The skill boundary is a single operator workflow: run a declarative policy that discovers an upstream value, checks conditions, updates target files, and prepares the resulting change for review. Install notes Install Updatecli from the project release page or one of the documented package methods. Create an updatecli.yaml policy describing sources, conditions, and targets. Run updatecli apply --config updatecli.yaml to execute the workflow.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines/)
