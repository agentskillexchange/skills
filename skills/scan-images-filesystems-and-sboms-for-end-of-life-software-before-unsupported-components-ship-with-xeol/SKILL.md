---
name: "Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol"
slug: "scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol"
description: "Find packages that are out of support even when they do not show up as a classic CVE finding yet."
github_stars: 435
verification: "security_reviewed"
source: "https://github.com/xeol-io/xeol"
author: "xeol-io"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "xeol-io/xeol"
  github_stars: 435
---

# Scan images filesystems and SBOMs for end-of-life software before unsupported components ship with Xeol

Find packages that are out of support even when they do not show up as a classic CVE finding yet.

## Prerequisites

Xeol CLI, a container image filesystem path or SBOM input, and optional CI integration for release gating.

## Installation

Use the upstream install or setup path that matches your environment:
- brew tap xeol-io/xeol
- brew install xeol
- docker run --rm \
- docker:yourrepo/yourimage:tag use images from the Docker daemon

Requirements and caveats from upstream:
- To run xeol from a Docker container so it can scan a running container, use the following command:
- --volume /var/run/docker.sock:/var/run/docker.sock \
- xeol can scan a variety of sources beyond those found in Docker.

Basic usage or getting-started notes:
- ### Recommended
- bash
- Check installation or check version of xeol

- Source: https://github.com/xeol-io/xeol
- Extracted from upstream docs: https://raw.githubusercontent.com/xeol-io/xeol/HEAD/README.md

## Documentation

- https://www.xeol.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-images-filesystems-and-sboms-for-end-of-life-software-before-unsupported-components-ship-with-xeol/)
