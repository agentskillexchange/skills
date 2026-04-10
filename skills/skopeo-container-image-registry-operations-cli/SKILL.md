---
name: Skopeo Container Image Registry Operations CLI
description: Skopeo is a command-line tool for working with container images and registries
  without requiring a running daemon. It can inspect, copy, delete, and sync container
  images across registries, supporting OCI and Docker v2 formats with rootless operation.
verification: security_reviewed
source: https://github.com/containers/skopeo
category:
- Security &amp; Verification
framework:
- Custom Agents
tool_ecosystem:
  github_repo: containers/skopeo
  github_stars: 10665
---
# Skopeo Container Image Registry Operations CLI

Overview
Skopeo is a command-line utility for performing operations on container images and image repositories. Developed by the Containers project (the same team behind Podman and Buildah), Skopeo operates without requiring root privileges or a running container daemon, making it ideal for CI/CD pipelines, security scanning workflows, and air-gapped deployment scenarios.
Key Features

Daemonless Operation: No Docker or container daemon required. Skopeo uses direct registry API calls, making it lightweight and suitable for restricted environments.
Cross-Registry Copy: Copy images between registries (e.g., Docker Hub to a private registry) without pulling the full image to the local machine, saving bandwidth and time.
Remote Inspection: Inspect image metadata, layers, labels, and architecture information from remote registries without downloading the image.
Multi-Format Support: Works with OCI images, Docker v2 images, local directories, docker-archive files, and container storage backends.
Registry Sync: Synchronize entire repositories between registries for air-gapped deployments and mirror management.
Rootless by Default: Most operations run without elevated privileges, improving security posture in automated pipelines.

How It Works
Skopeo communicates directly with container registries using the Docker Registry HTTP API V2 and OCI Distribution Spec. It supports multiple image transports including docker:// for remote registries, containers-storage: for local Podman/CRI-O stores, dir: for filesystem layouts, and docker-archive: for tarball files. Authentication credentials are read from $XDG_RUNTIME_DIR/containers/auth.json or can be configured via skopeo login.
Agent Integration
AI agents can use Skopeo to automate container image operations in CI/CD and security workflows. Common tasks include inspecting images before deployment to verify labels and layer counts, copying images between staging and production registries, syncing registries for air-gapped environments, and verifying image signatures. Its CLI interface and exit codes make it straightforward to integrate into automated pipelines.
Installation
# Fedora/RHEL
sudo dnf install skopeo

# Debian/Ubuntu
sudo apt install skopeo

# macOS
brew install skopeo

# From source (Go required)
git clone https://github.com/containers/skopeo
cd skopeo && make bin/skopeo
Usage Examples
# Inspect a remote image
skopeo inspect docker://docker.io/library/alpine:latest

# Copy between registries
skopeo copy docker://source-registry.io/myapp:v1 docker://dest-registry.io/myapp:v1

# Sync a repository
skopeo sync --src docker --dest dir registry.io/myrepo /local/backup/

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/skopeo-container-image-registry-operations-cli/)
