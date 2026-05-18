---
name: "Inspect and diff OCI images and registries with regctl"
slug: "inspect-and-diff-oci-images-and-registries-with-regctl"
description: "Use regctl when an agent needs to inspect manifests, compare image contents, or debug registry state without pulling whole images locally first."
github_stars: 1813
verification: "security_reviewed"
source: "https://github.com/regclient/regclient"
author: "regclient"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "regclient/regclient"
  github_stars: 1813
---

# Inspect and diff OCI images and registries with regctl

Use regctl when an agent needs to inspect manifests, compare image contents, or debug registry state without pulling whole images locally first.

## Prerequisites

regctl, network access to OCI registries, and registry credentials when needed.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install regctl from the project releases or your package manager, authenticate to any private registries you need, then use its inspect, manifest, diff, and copy commands in image review or incident workflows.
```

## Documentation

- https://regclient.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/)
