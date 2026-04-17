---
title: "Dive Docker Image Layer Explorer and Size Optimizer"
description: "Dive is a powerful open-source CLI tool written in Go that gives developers an interactive terminal UI for exploring the contents of Docker and OCI container images, layer by layer. Created by Alex Goodman (wagoodman), Dive has become the de facto standard for understanding and optimizing Docker image sizes, with over 53,000 GitHub stars and millions of Docker Hub pulls.\nHow Dive Works\nWhen you run dive , the tool pulls or references the target image and presents a split-pane TUI. The left pane shows each image layer with its size and command. The right pane displays the filesystem tree at that layer, with color-coded indicators showing which files were added, modified, or removed. This makes it trivially easy to spot bloated layers, unnecessary files, or duplicated content across layers.\nKey Features\nDive offers layer-by-layer filesystem exploration with full tree navigation. It calculates an image efficiency score that estimates wasted space from duplicated or moved files. The dive build command integrates directly into your workflow, letting you build a Docker image and immediately analyze it. For CI/CD pipelines, running with CI=true produces a pass/fail result based on configurable efficiency thresholds, making it suitable for automated image size enforcement in build pipelines.\nMultiple Container Engine Support\nDive supports Docker engine images, Docker tar archives, and Podman (on Linux). You can specify the source with the --source flag or use the source://image URI syntax. It also runs as a Docker container itself for environments where a native install is not desired.\nIntegration Points for AI Agents\nAI coding agents can leverage Dive in several workflows: automatically analyzing freshly built images to flag inefficiencies, running CI checks against Docker images, or generating optimization recommendations based on Dive output. The CI mode produces structured output that can be parsed programmatically, and the configurable efficiency thresholds make it straightforward to enforce size budgets in automated pipelines.\nInstallation\nDive is available via Homebrew (brew install dive), Snap, apt/deb, rpm, and as a Docker image (docker.io/wagoodman/dive). Prebuilt binaries for Linux, macOS, and Windows are available from the GitHub Releases page."
verification: security_reviewed
source: "https://github.com/wagoodman/dive"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "wagoodman/dive"
  github_stars: 53711
---

# Dive Docker Image Layer Explorer and Size Optimizer

Dive is a powerful open-source CLI tool written in Go that gives developers an interactive terminal UI for exploring the contents of Docker and OCI container images, layer by layer. Created by Alex Goodman (wagoodman), Dive has become the de facto standard for understanding and optimizing Docker image sizes, with over 53,000 GitHub stars and millions of Docker Hub pulls.
How Dive Works
When you run dive , the tool pulls or references the target image and presents a split-pane TUI. The left pane shows each image layer with its size and command. The right pane displays the filesystem tree at that layer, with color-coded indicators showing which files were added, modified, or removed. This makes it trivially easy to spot bloated layers, unnecessary files, or duplicated content across layers.
Key Features
Dive offers layer-by-layer filesystem exploration with full tree navigation. It calculates an image efficiency score that estimates wasted space from duplicated or moved files. The dive build command integrates directly into your workflow, letting you build a Docker image and immediately analyze it. For CI/CD pipelines, running with CI=true produces a pass/fail result based on configurable efficiency thresholds, making it suitable for automated image size enforcement in build pipelines.
Multiple Container Engine Support
Dive supports Docker engine images, Docker tar archives, and Podman (on Linux). You can specify the source with the --source flag or use the source://image URI syntax. It also runs as a Docker container itself for environments where a native install is not desired.
Integration Points for AI Agents
AI coding agents can leverage Dive in several workflows: automatically analyzing freshly built images to flag inefficiencies, running CI checks against Docker images, or generating optimization recommendations based on Dive output. The CI mode produces structured output that can be parsed programmatically, and the configurable efficiency thresholds make it straightforward to enforce size budgets in automated pipelines.
Installation
Dive is available via Homebrew (brew install dive), Snap, apt/deb, rpm, and as a Docker image (docker.io/wagoodman/dive). Prebuilt binaries for Linux, macOS, and Windows are available from the GitHub Releases page.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dive-docker-image-layer-explorer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dive-docker-image-layer-explorer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dive-docker-image-layer-explorer/)
