---
name: "Skopeo Container Image Registry Operations CLI"
slug: "skopeo-container-image-registry-operations-cli"
description: "Skopeo is a command-line tool for working with container images and registries without requiring a running daemon. It can inspect, copy, delete, and sync container images across registries, supporting OCI and Docker v2 formats with rootless operation."
github_stars: 10665
verification: "security_reviewed"
source: "https://github.com/containers/skopeo"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "containers/skopeo"
  github_stars: 10665
---

# Skopeo Container Image Registry Operations CLI

Skopeo is a command-line tool for working with container images and registries without requiring a running daemon. It can inspect, copy, delete, and sync container images across registries, supporting OCI and Docker v2 formats with rootless operation.

## Installation

Requirements and caveats from upstream:
- skopeo does not require the user to be running as root to do most of its operations.
- skopeo does not require a daemon to be running to perform its operations.
- skopeo can work with [OCI images](https://github.com/opencontainers/image-spec) as well as the original Docker v2 images.

Basic usage or getting-started notes:
- For example you can copy images from one registry to another, without requiring privilege.
- skopeo uses credentials from the --creds (for skopeo inspect|delete) or --src-creds|--dest-creds (for skopeo copy) flags, if set; otherwise it uses configuration set by skopeo login, podman login, buildah login, or do...

- Source: https://github.com/containers/skopeo
- Extracted from upstream docs: https://raw.githubusercontent.com/containers/skopeo/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/skopeo-container-image-registry-operations-cli/)
