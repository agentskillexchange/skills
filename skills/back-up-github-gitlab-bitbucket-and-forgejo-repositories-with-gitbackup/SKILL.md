---
name: "Back up GitHub, GitLab, Bitbucket, and Forgejo repositories with gitbackup"
slug: "back-up-github-gitlab-bitbucket-and-forgejo-repositories-with-gitbackup"
description: "Run repeatable cross-forge repository backup jobs from one config instead of hand-scripting clone and export steps per provider."
github_stars: 218
verification: "security_reviewed"
source: "https://github.com/amitsaha/gitbackup"
author: "Amit Saha"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "amitsaha/gitbackup"
  github_stars: 218
---

# Back up GitHub, GitLab, Bitbucket, and Forgejo repositories with gitbackup

Run repeatable cross-forge repository backup jobs from one config instead of hand-scripting clone and export steps per provider.

## Prerequisites

gitbackup binary or container image, forge access tokens, backup storage

## Installation

Use the upstream install or setup path that matches your environment:
- Docker images are published to [GitHub Container Registry](https://github.com/amitsaha/gitbackup/pkgs/container/gitbackup) on every release:
- docker pull ghcr.io/amitsaha/gitbackup:<version>
- docker run --rm \
- Docker Desktop for Mac runs containers inside a Linux VM and translates volume mounts through its filesystem layer (VirtioFS). Because of this translation, the container UID (65532) is mapped automatically — you do **...

Requirements and caveats from upstream:
- [Docker image](#docker-image)
- ### Docker image
- The container runs as a non-root user (nonroot, UID 65532). HTTPS cloning (-use-https-clone) is recommended inside containers because it requires no SSH key management.

Basic usage or getting-started notes:
- Run with HTTPS cloning (recommended):
- Starting with the 0.6 release, if you run gitbackup without specifying GITHUB_TOKEN, it will prompt you to complete

- Source: https://github.com/amitsaha/gitbackup
- Extracted from upstream docs: https://raw.githubusercontent.com/amitsaha/gitbackup/HEAD/README.md

## Documentation

- https://github.com/amitsaha/gitbackup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/back-up-github-gitlab-bitbucket-and-forgejo-repositories-with-gitbackup/)
