---
name: "Dive Docker Image Layer Explorer and Size Optimizer"
slug: "dive-docker-image-layer-explorer"
description: "Dive is a CLI tool for exploring Docker image layers, analyzing file system changes, and estimating wasted space. It helps developers optimize container image sizes by visualizing exactly what each layer adds, modifies, or removes."
github_stars: 53711
verification: "security_reviewed"
source: "https://github.com/wagoodman/dive"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "wagoodman/dive"
  github_stars: 53711
---

# Dive Docker Image Layer Explorer and Size Optimizer

Dive is a CLI tool for exploring Docker image layers, analyzing file system changes, and estimating wasted space. It helps developers optimize container image sizes by visualizing exactly what each layer adds, modifies, or removes.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run --rm -it \
- docker.io/wagoodman/dive:latest build -t <some-tag> .
- sudo snap install docker
- brew install dive

Requirements and caveats from upstream:
- **A tool for exploring a Docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image.**
- To analyze a Docker image simply run dive with an image tag/id/digest:
- or you can dive with Docker directly:

Basic usage or getting-started notes:
- # for example
- Additionally you can run this in your CI pipeline to ensure you're keeping wasted space to a minimum (this skips the UI):
- **Ubuntu/Debian**

- Source: https://github.com/wagoodman/dive
- Extracted from upstream docs: https://raw.githubusercontent.com/wagoodman/dive/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dive-docker-image-layer-explorer/)
