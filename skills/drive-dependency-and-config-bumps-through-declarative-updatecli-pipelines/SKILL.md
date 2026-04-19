---
title: "Drive dependency and config bumps through declarative Updatecli pipelines"
description: "Best for: teams that want an agent to watch upstream versions, patch config files or manifests, and produce reviewable update changes across repositories without hard-coding one package manager workflow. Updatecli is a declarative update policy engine. A policy file defines sources to discover a value, conditions to validate it, and targets to write the change. That makes it a strong fit for agent-driven maintenance runs where the goal is not just &#8220;check for updates&#8221; but &#8220;detect, validate, patch, and hand off a reviewable change set.&#8221; When to invoke it Invoke this skill when you want an agent to keep Docker tags, Helm values, GitOps manifests, CI images, or version pins current through one reproducible policy run. It is especially useful when the update spans multiple files or requires gating logic before a change should be written. Scope boundary This is not a general product listing for the Updatecli platform. The skill boundary is a single operator workflow: run a declarative policy that discovers an upstream value, checks conditions, updates target files, and prepares the resulting change for review. Install notes Install Updatecli from the project release page or one of the documented package methods. Create an updatecli.yaml policy describing sources, conditions, and targets. Run updatecli apply --config updatecli.yaml to execute the workflow."
source: "https://github.com/updatecli/updatecli"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "updatecli/updatecli"
  github_stars: 894
---

# Drive dependency and config bumps through declarative Updatecli pipelines

Best for: teams that want an agent to watch upstream versions, patch config files or manifests, and produce reviewable update changes across repositories without hard-coding one package manager workflow. Updatecli is a declarative update policy engine. A policy file defines sources to discover a value, conditions to validate it, and targets to write the change. That makes it a strong fit for agent-driven maintenance runs where the goal is not just &#8220;check for updates&#8221; but &#8220;detect, validate, patch, and hand off a reviewable change set.&#8221; When to invoke it Invoke this skill when you want an agent to keep Docker tags, Helm values, GitOps manifests, CI images, or version pins current through one reproducible policy run. It is especially useful when the update spans multiple files or requires gating logic before a change should be written. Scope boundary This is not a general product listing for the Updatecli platform. The skill boundary is a single operator workflow: run a declarative policy that discovers an upstream value, checks conditions, updates target files, and prepares the resulting change for review. Install notes Install Updatecli from the project release page or one of the documented package methods. Create an updatecli.yaml policy describing sources, conditions, and targets. Run updatecli apply --config updatecli.yaml to execute the workflow.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/drive-dependency-and-config-bumps-through-declarative-updatecli-pipelines/)
