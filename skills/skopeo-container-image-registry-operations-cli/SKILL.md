---
title: "Skopeo Container Image Registry Operations CLI"
description: "Skopeo is a command-line tool for working with container images and registries without requiring a running daemon. It can inspect, copy, delete, and sync container images across registries, supporting OCI and Docker v2 formats with rootless operation."
verification: "security_reviewed"
source: "https://github.com/containers/skopeo"
category: ["Security &amp; Verification"]
framework: ["Custom Agents"]
tool_ecosystem:
  github_repo: "containers/skopeo"
  github_stars: 10665
---

# Skopeo Container Image Registry Operations CLI

Skopeo is a command-line tool for working with container images and registries without requiring a running daemon. It can inspect, copy, delete, and sync container images across registries, supporting OCI and Docker v2 formats with rootless operation.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/skopeo-container-image-registry-operations-cli/)
