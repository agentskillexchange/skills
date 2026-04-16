---
title: "Inspect and diff OCI images and registries with regctl"
description: "Use regctl when an agent needs to inspect manifests, compare image contents, or debug registry state without pulling whole images locally first."
verification: "listed"
source: "https://github.com/regclient/regclient"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "regclient/regclient"
  github_stars: 1813
---

# Inspect and diff OCI images and registries with regctl

regctl gives agents an operator-grade registry workflow: inspect OCI image metadata, diff tags or manifests, copy artifacts, and debug registry state with explicit commands. Invoke it when the job is image and registry inspection, not when you just need to build containers or browse a registry UI. The boundary is clear: OCI registry diagnostics and artifact comparison, not a generic container platform or broad DevOps product card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/)
