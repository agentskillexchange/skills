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

Requirements and caveats from upstream:
- [![Docker Workflow Status](https://img.shields.io/github/actions/workflow/status/regclient/regclient/docker.yml?branch=main&label=Docker%20build)](https://github.com/regclient/regclient/actions/workflows/docker.yml)
- Efficiently query for pull rate limits used by Docker Hub.
- Import and export content into OCI Layouts and Docker formatted tar files.

Basic usage or getting-started notes:
- The project website includes [usage instructions](https://regclient.org/usage/regctl/) and a [CLI reference](https://regclient.org/cli/regctl/).
- Ability to run on a cron schedule, one time synchronization, or only report stale images.
- The project website includes [usage instructions](https://regclient.org/usage/regsync/) and a [CLI reference](https://regclient.org/cli/regsync/).

- Source: https://github.com/regclient/regclient
- Extracted from upstream docs: https://raw.githubusercontent.com/regclient/regclient/HEAD/README.md

## Documentation

- https://regclient.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-diff-oci-images-and-registries-with-regctl/)
